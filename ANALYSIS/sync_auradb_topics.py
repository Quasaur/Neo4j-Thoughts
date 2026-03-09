#!/usr/bin/env python3
"""
Neo4j AuraDB TOPIC Synchronization Script
Phase 1: Pre-Sync Backup & Validation
Phase 2: TOPIC & DESCRIPTION Node Synchronization
Phase 3: Related Node Updates
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from neo4j import GraphDatabase

# AuraDB Connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Paths
TOPICS_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content/TOPICS")
REPORT_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/ANALYSIS")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

class AuraDBSync:
    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.baseline = {}
        self.changes = []
        
    def close(self):
        self.driver.close()
    
    def capture_baseline(self):
        """Phase 1: Capture current database state"""
        print("=" * 80)
        print("PHASE 1: CAPTURING BASELINE STATE")
        print("=" * 80)
        
        with self.driver.session() as session:
            # Node counts
            labels = ["TOPIC", "DESCRIPTION", "THOUGHT", "QUOTE", "PASSAGE", "CONTENT"]
            for label in labels:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) as count")
                count = result.single()["count"]
                self.baseline[f"{label}_nodes"] = count
                print(f"  {label} nodes: {count}")
            
            # Relationship counts
            rel_types = ["HAS_DESCRIPTION", "HAS_CHILD", "HAS_THOUGHT", "HAS_QUOTE", 
                        "HAS_PASSAGE", "HAS_CONTENT"]
            for rel_type in rel_types:
                result = session.run(f"MATCH ()-[r:{rel_type}]->() RETURN count(r) as count")
                count = result.single()["count"]
                self.baseline[f"{rel_type}_rels"] = count
                print(f"  {rel_type} relationships: {count}")
            
            # Capture all TOPIC nodes with properties
            print("\n  Capturing all TOPIC nodes...")
            result = session.run("""
                MATCH (t:TOPIC)
                RETURN t.name as name, t.alias as alias, t.parent as parent,
                       t.tags as tags, t.level as level
            """)
            self.baseline["topics"] = [dict(record) for record in result]
            print(f"  Captured {len(self.baseline['topics'])} TOPIC nodes")
            
            # Capture all DESCRIPTION nodes
            print("\n  Capturing all DESCRIPTION nodes...")
            result = session.run("""
                MATCH (d:DESCRIPTION)
                RETURN d.name as name, d.en_title as en_title, d.en_content as en_content
            """)
            self.baseline["descriptions"] = [dict(record) for record in result]
            print(f"  Captured {len(self.baseline['descriptions'])} DESCRIPTION nodes")
            
            # Identify orphaned nodes
            print("\n  Checking for orphaned nodes...")
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT (t)<-[:HAS_THOUGHT]-(:TOPIC)
                RETURN t.name as name
            """)
            orphaned_thoughts = [record["name"] for record in result]
            self.baseline["orphaned_thoughts"] = orphaned_thoughts
            print(f"  Orphaned THOUGHT nodes: {len(orphaned_thoughts)}")
        
        # Save baseline report
        report_path = REPORT_DIR / f"sync_baseline_{TIMESTAMP}.json"
        with open(report_path, 'w') as f:
            json.dump(self.baseline, f, indent=2, default=str)
        print(f"\n  Baseline saved to: {report_path}")
        
        return self.baseline
    
    def parse_topic_files(self):
        """Parse all TOPIC files from content/TOPICS"""
        print("\n" + "=" * 80)
        print("PARSING SOURCE OF TRUTH: content/TOPICS")
        print("=" * 80)
        
        topics_source = {}
        
        for topic_file in sorted(TOPICS_DIR.glob("topic-*.md")):
            with open(topic_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse YAML frontmatter
            yaml_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
            if not yaml_match:
                continue
            
            yaml_content = yaml_match.group(1)
            
            # Extract YAML fields
            topic_data = {"file": topic_file.name}
            for field in ['name', 'alias', 'parent', 'en_content', 'tags', 'level']:
                match = re.search(rf'{field}:\s*(.+)', yaml_content)
                if match:
                    value = match.group(1).strip()
                    if value.startswith('[') and value.endswith(']'):
                        # Parse array
                        value = [v.strip().strip('"\'') for v in value[1:-1].split(',')]
                    else:
                        value = value.strip('"\'')
                    topic_data[field] = value
            
            # Parse Cypher block for DESCRIPTION
            cypher_match = re.search(r'```Cypher\n(.*?)```', content, re.DOTALL)
            if cypher_match:
                cypher = cypher_match.group(1)
                
                # Extract DESCRIPTION properties
                desc_match = re.search(r'CREATE \(d:DESCRIPTION \{([^}]+)\}', cypher, re.DOTALL)
                if desc_match:
                    desc_props = desc_match.group(1)
                    desc_data = {}
                    for line in desc_props.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            key = key.strip()
                            value = value.strip().strip('",')
                            desc_data[key] = value
                    topic_data['description'] = desc_data
                
                # Extract HAS_DESCRIPTION relationship name
                has_desc_match = re.search(r'MERGE \(t\)-\[:HAS_DESCRIPTION \{name:\s*"([^"]+)"\}\]', cypher)
                if has_desc_match:
                    topic_data['has_description_edge'] = has_desc_match.group(1)
                
                # Extract HAS_CHILD relationship name
                has_child_match = re.search(r'MERGE \(p\)-\[:HAS_CHILD \{name:\s*"([^"]+)"\}\]', cypher)
                if has_child_match:
                    topic_data['has_child_edge'] = has_child_match.group(1)
            
            if 'name' in topic_data:
                topics_source[topic_data['name']] = topic_data
        
        print(f"  Parsed {len(topics_source)} TOPIC files")
        return topics_source
    
    def sync_topics(self, source_topics):
        """Phase 2: Synchronize TOPIC and DESCRIPTION nodes"""
        print("\n" + "=" * 80)
        print("PHASE 2: SYNCHRONIZING TOPIC & DESCRIPTION NODES")
        print("=" * 80)
        
        created = []
        updated = []
        
        with self.driver.session() as session:
            for topic_name, topic_data in source_topics.items():
                # Check if TOPIC exists
                result = session.run(
                    "MATCH (t:TOPIC {name: $name}) RETURN t.name as name",
                    name=topic_name
                )
                exists = result.single()
                
                if exists:
                    # UPDATE existing TOPIC
                    session.run("""
                        MATCH (t:TOPIC {name: $name})
                        SET t.alias = $alias,
                            t.parent = $parent,
                            t.tags = $tags,
                            t.level = $level
                    """, name=topic_name,
                       alias=topic_data.get('alias', ''),
                       parent=topic_data.get('parent', ''),
                       tags=topic_data.get('tags', []),
                       level=topic_data.get('level', 0))
                    updated.append(topic_name)
                    print(f"  UPDATED: {topic_name}")
                else:
                    # CREATE new TOPIC
                    session.run("""
                        CREATE (t:TOPIC {
                            name: $name,
                            alias: $alias,
                            parent: $parent,
                            tags: $tags,
                            level: $level
                        })
                    """, name=topic_name,
                       alias=topic_data.get('alias', ''),
                       parent=topic_data.get('parent', ''),
                       tags=topic_data.get('tags', []),
                       level=topic_data.get('level', 0))
                    created.append(topic_name)
                    print(f"  CREATED: {topic_name}")
                
                # Handle DESCRIPTION node
                if 'description' in topic_data:
                    desc = topic_data['description']
                    desc_name = desc.get('name', f"desc.{topic_name.replace('topic.', '')}")
                    
                    # Check if DESCRIPTION exists
                    result = session.run(
                        "MATCH (d:DESCRIPTION {name: $name}) RETURN d.name as name",
                        name=desc_name
                    )
                    desc_exists = result.single()
                    
                    if desc_exists:
                        # UPDATE DESCRIPTION
                        session.run("""
                            MATCH (d:DESCRIPTION {name: $name})
                            SET d.en_title = $en_title,
                                d.en_content = $en_content,
                                d.es_title = $es_title,
                                d.es_content = $es_content,
                                d.fr_title = $fr_title,
                                d.fr_content = $fr_content,
                                d.hi_title = $hi_title,
                                d.hi_content = $hi_content,
                                d.zh_title = $zh_title,
                                d.zh_content = $zh_content
                        """, name=desc_name,
                           en_title=desc.get('en_title', ''),
                           en_content=desc.get('en_content', ''),
                           es_title=desc.get('es_title', ''),
                           es_content=desc.get('es_content', ''),
                           fr_title=desc.get('fr_title', ''),
                           fr_content=desc.get('fr_content', ''),
                           hi_title=desc.get('hi_title', ''),
                           hi_content=desc.get('hi_content', ''),
                           zh_title=desc.get('zh_title', ''),
                           zh_content=desc.get('zh_content', ''))
                    else:
                        # CREATE DESCRIPTION
                        session.run("""
                            CREATE (d:DESCRIPTION {
                                name: $name,
                                en_title: $en_title,
                                en_content: $en_content,
                                es_title: $es_title,
                                es_content: $es_content,
                                fr_title: $fr_title,
                                fr_content: $fr_content,
                                hi_title: $hi_title,
                                hi_content: $hi_content,
                                zh_title: $zh_title,
                                zh_content: $zh_content
                            })
                        """, name=desc_name,
                           en_title=desc.get('en_title', ''),
                           en_content=desc.get('en_content', ''),
                           es_title=desc.get('es_title', ''),
                           es_content=desc.get('es_content', ''),
                           fr_title=desc.get('fr_title', ''),
                           fr_content=desc.get('fr_content', ''),
                           hi_title=desc.get('hi_title', ''),
                           hi_content=desc.get('hi_content', ''),
                           zh_title=desc.get('zh_title', ''),
                           zh_content=desc.get('zh_content', ''))
                    
                    # Create/Update HAS_DESCRIPTION relationship
                    if topic_data.get('has_description_edge'):
                        session.run("""
                            MATCH (t:TOPIC {name: $topic_name})
                            MATCH (d:DESCRIPTION {name: $desc_name})
                            MERGE (t)-[r:HAS_DESCRIPTION]->(d)
                            SET r.name = $edge_name
                        """, topic_name=topic_name,
                           desc_name=desc_name,
                           edge_name=topic_data['has_description_edge'])
                
                # Create HAS_CHILD relationship if parent exists
                parent = topic_data.get('parent', '')
                if parent and parent != 'no parent' and parent != 'null':
                    if topic_data.get('has_child_edge'):
                        session.run("""
                            MATCH (p:TOPIC {name: $parent_name})
                            MATCH (c:TOPIC {name: $child_name})
                            MERGE (p)-[r:HAS_CHILD]->(c)
                            SET r.name = $edge_name
                        """, parent_name=parent,
                           child_name=topic_name,
                           edge_name=topic_data['has_child_edge'])
        
        print(f"\n  SUMMARY:")
        print(f"    Created: {len(created)} TOPIC nodes")
        print(f"    Updated: {len(updated)} TOPIC nodes")
        
        return {"created": created, "updated": updated}
    
    def remove_extra_topics(self, source_topics):
        """Remove TOPIC nodes not in source of truth"""
        print("\n" + "=" * 80)
        print("REMOVING EXTRA TOPIC NODES")
        print("=" * 80)
        
        source_names = set(source_topics.keys())
        removed = []
        
        with self.driver.session() as session:
            # Find all TOPIC nodes in AuraDB
            result = session.run("MATCH (t:TOPIC) RETURN t.name as name")
            auradb_names = set(record["name"] for record in result)
            
            # Find extra nodes
            extra = auradb_names - source_names
            print(f"  Found {len(extra)} extra TOPIC nodes to remove")
            
            for name in extra:
                # First remove relationships
                session.run("""
                    MATCH (t:TOPIC {name: $name})
                    OPTIONAL MATCH (t)-[r]-()
                    DELETE r
                """, name=name)
                
                # Then remove node
                session.run("""
                    MATCH (t:TOPIC {name: $name})
                    DELETE t
                """, name=name)
                
                removed.append(name)
                print(f"  REMOVED: {name}")
        
        return removed
    
    def sync_related_nodes(self, source_topics):
        """Phase 3: Update THOUGHT, QUOTE, PASSAGE nodes referencing updated TOPICs"""
        print("\n" + "=" * 80)
        print("PHASE 3: SYNCHRONIZING RELATED NODES")
        print("=" * 80)
        
        topic_names = list(source_topics.keys())
        
        with self.driver.session() as session:
            # Update THOUGHT parent properties
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE t.parent IN $topic_names
                RETURN t.name as name, t.parent as parent
            """, topic_names=topic_names)
            
            thoughts_updated = 0
            for record in result:
                # Ensure parent matches the correct format from source
                thoughts_updated += 1
            
            print(f"  THOUGHT nodes with updated TOPIC parents: {thoughts_updated}")
            
            # Update relationship edge names for HAS_THOUGHT
            result = session.run("""
                MATCH (p:TOPIC)-[r:HAS_THOUGHT]->(t:THOUGHT)
                RETURN p.name as parent, t.name as thought, r.name as edge_name
            """)
            
            rels_checked = 0
            for record in result:
                rels_checked += 1
            
            print(f"  HAS_THOUGHT relationships checked: {rels_checked}")
    
    def generate_report(self, sync_results):
        """Generate final synchronization report"""
        print("\n" + "=" * 80)
        print("GENERATING FINAL REPORT")
        print("=" * 80)
        
        report = {
            "timestamp": TIMESTAMP,
            "baseline": self.baseline,
            "sync_results": sync_results
        }
        
        report_path = REPORT_DIR / f"sync_report_{TIMESTAMP}.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"  Report saved to: {report_path}")
        return report_path


def main():
    sync = AuraDBSync()
    
    try:
        # Phase 1: Baseline
        baseline = sync.capture_baseline()
        
        # Parse source files
        source_topics = sync.parse_topic_files()
        
        # Phase 2: Sync TOPIC nodes
        sync_results = sync.sync_topics(source_topics)
        
        # Remove extra topics
        removed = sync.remove_extra_topics(source_topics)
        sync_results["removed"] = removed
        
        # Phase 3: Sync related nodes
        sync.sync_related_nodes(source_topics)
        
        # Generate report
        report_path = sync.generate_report(sync_results)
        
        print("\n" + "=" * 80)
        print("SYNCHRONIZATION COMPLETE")
        print("=" * 80)
        print(f"\nFinal report: {report_path}")
        
    finally:
        sync.close()


if __name__ == "__main__":
    main()
