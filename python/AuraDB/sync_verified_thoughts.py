#!/usr/bin/env python3
"""
Sync verified THOUGHT markdown files to Neo4j AuraDB.
- Processes files with verified: true in YAML frontmatter
- Fixes Cypher block errors before execution
- Creates missing THOUGHT nodes, CONTENT nodes, and HAS_THOUGHT relationships
- Creates missing parent TOPIC nodes if needed
- Tracks processed files in docs/reports/thoughts_uploaded.md
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from neo4j import GraphDatabase

# Neo4j AuraDB connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Directories
THOUGHTS_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content/THOUGHTS")
TOPICS_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/content/TOPICS")
REPORT_FILE = Path("/Users/quasaur/Developer/Neo4j-Thoughts/docs/reports/thoughts_uploaded.md")


class ThoughtSync:
    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.report = {
            'processed': [],
            'created': [],
            'updated': [],
            'skipped': [],
            'errors': [],
            'topics_created': []
        }
    
    def close(self):
        self.driver.close()
    
    def verify_connection(self):
        """Verify connection to AuraDB"""
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                record = result.single()
                print(f"✓ Connected to Neo4j AuraDB successfully")
                return True
        except Exception as e:
            print(f"✗ Failed to connect to Neo4j: {e}")
            return False
    
    def extract_yaml_frontmatter(self, content):
        """Extract YAML frontmatter from markdown content"""
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except Exception as e:
                print(f"  Warning: Failed to parse YAML: {e}")
                return None
        return None
    
    def extract_cypher_block(self, content):
        """Extract Cypher block from markdown content"""
        match = re.search(r'```[Cc]ypher\s*\n(.*?)```', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    
    def fix_cypher_errors(self, cypher_block, yaml_data):
        """Fix known errors in Cypher blocks"""
        fixes_applied = []
        parent = yaml_data.get('parent', '')
        
        # Fix 1: Empty parent name in MATCH
        if 'MATCH (parent:TOPIC {name: ""})' in cypher_block and parent:
            cypher_block = cypher_block.replace(
                'MATCH (parent:TOPIC {name: ""})',
                f'MATCH (parent:TOPIC {{name: "{parent}"}})'
            )
            fixes_applied.append(f"Fixed empty parent name -> '{parent}'")
        
        # Fix 2: Typo "tooic" -> "topic"
        if 'tooic.' in cypher_block:
            cypher_block = cypher_block.replace('tooic.', 'topic.')
            fixes_applied.append("Fixed typo 'tooic' -> 'topic'")
        
        # Fix 3: Fix relationship edge name if parent was fixed
        if fixes_applied and parent:
            thought_name = yaml_data.get('name', '').replace('thought.', '')
            # Fix edge name pattern like "t.edge.->THOUGHT_NAME" -> "t.edge.PARENT->THOUGHT_NAME"
            wrong_edge = f't.edge.->{thought_name}'
            correct_edge = f't.edge.{parent.replace("topic.", "")}->{thought_name}'
            if wrong_edge in cypher_block:
                cypher_block = cypher_block.replace(wrong_edge, correct_edge)
                fixes_applied.append(f"Fixed edge name -> '{correct_edge}'")
        
        # Fix 4: Fix missing semicolon after MERGE before ON CREATE SET
        # Pattern: MERGE ... )\nON CREATE SET -> MERGE ... )\n;\nON CREATE SET
        cypher_block = re.sub(
            r'(MERGE\s*\([^)]+\)\s*ON CREATE SET)',
            r';\n\1',
            cypher_block
        )
        
        return cypher_block, fixes_applied
    
    def split_cypher_statements(self, cypher_block):
        """Split Cypher block into individual statements"""
        # Remove comments
        lines = cypher_block.split('\n')
        cleaned_lines = []
        for line in lines:
            # Skip comment lines but keep empty lines for structure
            stripped = line.strip()
            if stripped.startswith('//'):
                continue
            cleaned_lines.append(line)
        
        # Join and split by semicolons
        cleaned = '\n'.join(cleaned_lines)
        statements = [s.strip() for s in cleaned.split(';') if s.strip()]
        return statements
    
    def get_verified_thought_files(self):
        """Get all markdown files with verified: true"""
        verified_files = []
        for md_file in sorted(THOUGHTS_DIR.glob("*.md")):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            yaml_data = self.extract_yaml_frontmatter(content)
            if yaml_data and yaml_data.get('verified') == True:
                verified_files.append({
                    'filepath': md_file,
                    'filename': md_file.name,
                    'yaml': yaml_data,
                    'content': content
                })
        
        return verified_files
    
    def check_thought_exists(self, thought_name):
        """Check if a THOUGHT node exists in Neo4j"""
        with self.driver.session() as session:
            result = session.run(
                "MATCH (t:THOUGHT {name: $name}) RETURN count(t) as count",
                name=thought_name
            )
            record = result.single()
            return record['count'] > 0
    
    def check_content_exists(self, content_name):
        """Check if a CONTENT node exists in Neo4j"""
        with self.driver.session() as session:
            result = session.run(
                "MATCH (c:CONTENT {name: $name}) RETURN count(c) as count",
                name=content_name
            )
            record = result.single()
            return record['count'] > 0
    
    def check_topic_exists(self, topic_name):
        """Check if a TOPIC node exists in Neo4j"""
        with self.driver.session() as session:
            result = session.run(
                "MATCH (t:TOPIC {name: $name}) RETURN count(t) as count",
                name=topic_name
            )
            record = result.single()
            return record['count'] > 0
    
    def extract_topic_from_filename(self, topic_name):
        """Convert topic.name to filename format"""
        # topic.APOCALYPSE -> topic-APOCALYPSE.md
        name_part = topic_name.replace('topic.', '')
        return f"topic-{name_part}.md"
    
    def create_topic_from_file(self, topic_name):
        """Create a TOPIC node from its markdown file"""
        filename = self.extract_topic_from_filename(topic_name)
        topic_file = TOPICS_DIR / filename
        
        if not topic_file.exists():
            return False, f"Topic file not found: {filename}"
        
        with open(topic_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cypher = self.extract_cypher_block(content)
        if not cypher:
            return False, f"No Cypher block found in {filename}"
        
        # Execute the topic creation cypher
        statements = self.split_cypher_statements(cypher)
        try:
            with self.driver.session() as session:
                for stmt in statements:
                    if stmt.strip():
                        session.run(stmt)
                return True, f"Created TOPIC: {topic_name}"
        except Exception as e:
            return False, f"Error creating TOPIC {topic_name}: {e}"
    
    def create_thought_from_yaml(self, yaml_data):
        """Create THOUGHT and CONTENT nodes using YAML data"""
        thought_name = yaml_data['name']
        thought_base = thought_name.replace('thought.', '')
        content_name = f"content.{thought_base}"
        parent = yaml_data.get('parent', '')
        
        try:
            with self.driver.session() as session:
                # 1. Create THOUGHT node
                session.run("""
                    CREATE (t:THOUGHT {
                        name: $name,
                        alias: $alias,
                        parent: $parent,
                        tags: $tags,
                        level: $level
                    })
                """, 
                    name=thought_name,
                    alias=yaml_data.get('alias', ''),
                    parent=parent,
                    tags=yaml_data.get('tags', []),
                    level=yaml_data.get('level', 5)
                )
                
                # 2. Create CONTENT node
                session.run("""
                    CREATE (c:CONTENT {
                        name: $name,
                        ctype: 'THOUGHT',
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
                """,
                    name=content_name,
                    en_title=yaml_data.get('en_title', yaml_data.get('alias', '')),
                    en_content=yaml_data.get('en_content', ''),
                    es_title=yaml_data.get('es_title', ''),
                    es_content=yaml_data.get('es_content', ''),
                    fr_title=yaml_data.get('fr_title', ''),
                    fr_content=yaml_data.get('fr_content', ''),
                    hi_title=yaml_data.get('hi_title', ''),
                    hi_content=yaml_data.get('hi_content', ''),
                    zh_title=yaml_data.get('zh_title', ''),
                    zh_content=yaml_data.get('zh_content', '')
                )
                
                # 3. Create HAS_CONTENT relationship
                session.run("""
                    MATCH (t:THOUGHT {name: $thought_name})
                    MATCH (c:CONTENT {name: $content_name})
                    MERGE (t)-[r:HAS_CONTENT]->(c)
                    ON CREATE SET r.name = $edge_name
                """,
                    thought_name=thought_name,
                    content_name=content_name,
                    edge_name=f"t.edge.{thought_base}"
                )
                
                # 4. Create HAS_THOUGHT relationship to parent if parent exists
                if parent:
                    parent_short = parent.replace('topic.', '')
                    session.run("""
                        MATCH (parent:TOPIC {name: $parent})
                        MATCH (t:THOUGHT {name: $thought_name})
                        MERGE (parent)-[r:HAS_THOUGHT]->(t)
                        ON CREATE SET r.name = $edge_name
                    """,
                        parent=parent,
                        thought_name=thought_name,
                        edge_name=f"t.edge.{parent_short}->{thought_base}"
                    )
                
                return True, None
        except Exception as e:
            return False, str(e)
    
    def update_thought_properties(self, thought_name, yaml_data):
        """Update existing THOUGHT node properties from YAML"""
        updates = []
        parent = yaml_data.get('parent', '')
        
        with self.driver.session() as session:
            # Get current properties
            result = session.run(
                "MATCH (t:THOUGHT {name: $name}) RETURN t",
                name=thought_name
            )
            record = result.single()
            if not record:
                return []
            
            current = dict(record['t'])
            
            # Compare and build updates
            fields = ['alias', 'parent', 'tags', 'level']
            set_clauses = []
            params = {'name': thought_name}
            
            for field in fields:
                if field in yaml_data:
                    yaml_value = yaml_data[field]
                    db_value = current.get(field)
                    
                    # Normalize for comparison
                    if field == 'tags':
                        if isinstance(yaml_value, str):
                            yaml_value = [t.strip() for t in yaml_value.split(',')]
                        if isinstance(db_value, list) and isinstance(yaml_value, list):
                            if sorted(db_value) != sorted(yaml_value):
                                set_clauses.append(f"t.{field} = ${field}")
                                params[field] = yaml_value
                                updates.append(f"{field}: {db_value} -> {yaml_value}")
                    elif yaml_value != db_value:
                        set_clauses.append(f"t.{field} = ${field}")
                        params[field] = yaml_value
                        updates.append(f"{field}: {db_value} -> {yaml_value}")
            
            if set_clauses:
                query = f"MATCH (t:THOUGHT {{name: $name}}) SET {', '.join(set_clauses)}"
                session.run(query, params)
            
            # Check/fix parent relationship
            if parent:
                result = session.run("""
                    MATCH (t:THOUGHT {name: $thought_name})
                    MATCH (parent:TOPIC {name: $parent})
                    MATCH (parent)-[r:HAS_THOUGHT]->(t)
                    RETURN count(r) as count
                """, thought_name=thought_name, parent=parent)
                
                if result.single()['count'] == 0:
                    # Relationship doesn't exist, create it
                    thought_base = thought_name.replace('thought.', '')
                    parent_short = parent.replace('topic.', '')
                    session.run("""
                        MATCH (t:THOUGHT {name: $thought_name})
                        MATCH (parent:TOPIC {name: $parent})
                        MERGE (parent)-[r:HAS_THOUGHT]->(t)
                        ON CREATE SET r.name = $edge_name
                    """, 
                        thought_name=thought_name,
                        parent=parent,
                        edge_name=f"t.edge.{parent_short}->{thought_base}"
                    )
                    updates.append(f"HAS_THOUGHT relationship to {parent} created")
        
        return updates
    
    def update_content_properties(self, content_name, yaml_data):
        """Update existing CONTENT node properties from YAML"""
        updates = []
        
        with self.driver.session() as session:
            result = session.run(
                "MATCH (c:CONTENT {name: $name}) RETURN c",
                name=content_name
            )
            record = result.single()
            if not record:
                return []
            
            current = dict(record['c'])
            
            # Compare and build updates for content fields
            content_fields = ['en_content', 'es_content', 'fr_content', 'hi_content', 'zh_content',
                            'en_title', 'es_title', 'fr_title', 'hi_title', 'zh_title']
            set_clauses = []
            params = {'name': content_name}
            
            for field in content_fields:
                if field in yaml_data:
                    yaml_value = yaml_data[field]
                    db_value = current.get(field)
                    if yaml_value != db_value:
                        set_clauses.append(f"c.{field} = ${field}")
                        params[field] = yaml_value
                        updates.append(f"{field}: updated")
            
            if set_clauses:
                query = f"MATCH (c:CONTENT {{name: $name}}) SET {', '.join(set_clauses)}"
                session.run(query, params)
        
        return updates
    
    def process_file(self, file_info):
        """Process a single verified thought file"""
        filename = file_info['filename']
        yaml_data = file_info['yaml']
        content = file_info['content']
        
        thought_name = yaml_data.get('name')
        parent_topic = yaml_data.get('parent')
        
        print(f"\n📄 Processing: {filename}")
        print(f"   THOUGHT: {thought_name}")
        print(f"   Parent: {parent_topic}")
        
        # Check if parent TOPIC exists
        if parent_topic and not self.check_topic_exists(parent_topic):
            print(f"   ⚠️  Parent TOPIC not found: {parent_topic}")
            print(f"   🔄 Creating parent TOPIC...")
            success, msg = self.create_topic_from_file(parent_topic)
            if success:
                print(f"   ✓ {msg}")
                self.report['topics_created'].append(parent_topic)
            else:
                print(f"   ✗ Failed to create parent TOPIC: {msg}")
                self.report['errors'].append({'file': filename, 'error': f"Parent TOPIC creation failed: {msg}"})
                return False
        
        # Check if THOUGHT exists
        thought_exists = self.check_thought_exists(thought_name)
        
        if thought_exists:
            print(f"   ℹ️  THOUGHT exists, checking for updates...")
            
            # Update THOUGHT properties
            thought_updates = self.update_thought_properties(thought_name, yaml_data)
            
            # Update CONTENT properties
            content_name = f"content.{thought_name.replace('thought.', '')}"
            content_updates = self.update_content_properties(content_name, yaml_data)
            
            if thought_updates or content_updates:
                print(f"   ✓ Updated properties:")
                for update in thought_updates + content_updates:
                    print(f"      - {update}")
                self.report['updated'].append({
                    'file': filename,
                    'thought': thought_name,
                    'changes': thought_updates + content_updates
                })
            else:
                print(f"   ✓ No updates needed")
                self.report['skipped'].append(filename)
        else:
            print(f"   🔄 Creating THOUGHT node...")
            success, error = self.create_thought_from_yaml(yaml_data)
            
            if success:
                print(f"   ✓ Created THOUGHT: {thought_name}")
                self.report['created'].append(filename)
            else:
                print(f"   ✗ Error creating THOUGHT: {error}")
                self.report['errors'].append({'file': filename, 'error': error})
                return False
        
        self.report['processed'].append(filename)
        return True
    
    def update_report_file(self):
        """Update the thoughts_uploaded.md report file"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Read existing content if file exists
        existing_content = ""
        if REPORT_FILE.exists():
            with open(REPORT_FILE, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        
        # Build new content
        lines = [
            "# Thoughts Uploaded to Neo4j AuraDB",
            "",
            f"**Last Updated:** {now}",
            "",
            "## Summary",
            "",
            f"- **Total Files Processed:** {len(self.report['processed'])}",
            f"- **THOUGHTs Created:** {len(self.report['created'])}",
            f"- **THOUGHTs Updated:** {len(self.report['updated'])}",
            f"- **TOPICs Created:** {len(self.report['topics_created'])}",
            f"- **Errors:** {len(self.report['errors'])}",
            "",
            "## Processed Files",
            ""
        ]
        
        if self.report['processed']:
            lines.append("| Filename | Status | Details |")
            lines.append("|----------|--------|---------|")
            
            for filename in self.report['processed']:
                # Determine status
                if filename in self.report['created']:
                    status = "✅ Created"
                    details = "New THOUGHT node inserted"
                elif any(u['file'] == filename for u in self.report['updated']):
                    status = "🔄 Updated"
                    update_info = next(u for u in self.report['updated'] if u['file'] == filename)
                    details = f"{len(update_info['changes'])} field(s) updated"
                else:
                    status = "⏭️  Skipped"
                    details = "No changes needed"
                
                lines.append(f"| {filename} | {status} | {details} |")
        else:
            lines.append("*No files processed yet*")
        
        lines.extend([
            "",
            "## Created THOUGHTs",
            ""
        ])
        
        if self.report['created']:
            for filename in self.report['created']:
                lines.append(f"- {filename}")
        else:
            lines.append("*No THOUGHTs created in this batch*")
        
        lines.extend([
            "",
            "## Updated THOUGHTs",
            ""
        ])
        
        if self.report['updated']:
            for update in self.report['updated']:
                lines.append(f"- **{update['file']}** ({update['thought']})")
                for change in update['changes']:
                    lines.append(f"  - {change}")
        else:
            lines.append("*No THOUGHTs updated in this batch*")
        
        lines.extend([
            "",
            "## Created Parent TOPICs",
            ""
        ])
        
        if self.report['topics_created']:
            for topic in self.report['topics_created']:
                lines.append(f"- {topic}")
        else:
            lines.append("*No TOPICs created in this batch*")
        
        lines.extend([
            "",
            "## Errors",
            ""
        ])
        
        if self.report['errors']:
            for error in self.report['errors']:
                lines.append(f"- **{error['file']}**: {error['error']}")
        else:
            lines.append("*No errors*")
        
        lines.extend([
            "",
            "---",
            "",
            "*This file is automatically generated by the sync script.*"
        ])
        
        # Write to file
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"\n📝 Report updated: {REPORT_FILE}")
    
    def print_summary(self):
        """Print final summary"""
        print("\n" + "="*70)
        print("SYNC SUMMARY")
        print("="*70)
        print(f"\n📊 Files Processed: {len(self.report['processed'])}")
        print(f"   ✓ Created: {len(self.report['created'])}")
        print(f"   🔄 Updated: {len(self.report['updated'])}")
        print(f"   ⏭️  Skipped: {len(self.report['skipped'])}")
        print(f"   ✗ Errors: {len(self.report['errors'])}")
        print(f"\n📊 Parent TOPICs Created: {len(self.report['topics_created'])}")
        
        if self.report['errors']:
            print("\n❌ ERRORS:")
            for error in self.report['errors']:
                print(f"   - {error['file']}: {error['error']}")
        
        print("\n" + "="*70)


def main():
    sync = ThoughtSync()
    
    try:
        # Verify connection
        if not sync.verify_connection():
            return
        
        # Get verified files
        print("\n🔍 Scanning for verified THOUGHT files...")
        verified_files = sync.get_verified_thought_files()
        print(f"   Found {len(verified_files)} files with verified: true")
        
        if not verified_files:
            print("\n⚠️  No verified files to process")
            return
        
        # Process each file
        print("\n🚀 Starting sync...")
        for file_info in verified_files:
            sync.process_file(file_info)
        
        # Update report file
        sync.update_report_file()
        
        # Print summary
        sync.print_summary()
        
    finally:
        sync.close()


if __name__ == "__main__":
    main()
