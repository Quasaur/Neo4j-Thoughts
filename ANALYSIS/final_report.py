#!/usr/bin/env python3
"""
Phase 5: Final Validation & Comprehensive Report
"""

import json
from datetime import datetime
from neo4j import GraphDatabase
from pathlib import Path

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
REPORT_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/ANALYSIS")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

def generate_final_report():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        print("=" * 80)
        print("PHASE 5: FINAL VALIDATION & REPORT")
        print("=" * 80)
        
        report = {
            "timestamp": TIMESTAMP,
            "summary": {},
            "node_counts": {},
            "relationship_counts": {},
            "orphaned_nodes": {},
            "verification_checks": {}
        }
        
        with driver.session() as session:
            # Node counts
            print("\n1. NODE COUNTS")
            print("-" * 40)
            labels = ["TOPIC", "DESCRIPTION", "THOUGHT", "QUOTE", "PASSAGE", "CONTENT"]
            for label in labels:
                result = session.run(f"MATCH (n:{label}) RETURN count(n) as count")
                count = result.single()["count"]
                report["node_counts"][label] = count
                print(f"   {label}: {count}")
            
            # Relationship counts
            print("\n2. RELATIONSHIP COUNTS")
            print("-" * 40)
            rel_types = ["HAS_DESCRIPTION", "HAS_CHILD", "HAS_THOUGHT", 
                        "HAS_QUOTE", "HAS_PASSAGE", "HAS_CONTENT"]
            for rel_type in rel_types:
                result = session.run(f"MATCH ()-[r:{rel_type}]->() RETURN count(r) as count")
                count = result.single()["count"]
                report["relationship_counts"][rel_type] = count
                print(f"   {rel_type}: {count}")
            
            # Check for orphaned nodes
            print("\n3. ORPHANED NODES CHECK")
            print("-" * 40)
            
            # Orphaned THOUGHTs
            result = session.run("""
                MATCH (t:THOUGHT)
                WHERE NOT (t)<-[:HAS_THOUGHT]-(:TOPIC)
                RETURN count(t) as count
            """)
            orphaned_thoughts = result.single()["count"]
            report["orphaned_nodes"]["THOUGHT"] = orphaned_thoughts
            print(f"   Orphaned THOUGHTs: {orphaned_thoughts}")
            
            # Orphaned QUOTEs
            result = session.run("""
                MATCH (q:QUOTE)
                WHERE NOT (q)<-[:HAS_QUOTE]-(:TOPIC)
                RETURN count(q) as count
            """)
            orphaned_quotes = result.single()["count"]
            report["orphaned_nodes"]["QUOTE"] = orphaned_quotes
            print(f"   Orphaned QUOTEs: {orphaned_quotes}")
            
            # Orphaned PASSAGEs
            result = session.run("""
                MATCH (p:PASSAGE)
                WHERE NOT (p)<-[:HAS_PASSAGE]-(:TOPIC)
                RETURN count(p) as count
            """)
            orphaned_passages = result.single()["count"]
            report["orphaned_nodes"]["PASSAGE"] = orphaned_passages
            print(f"   Orphaned PASSAGEs: {orphaned_passages}")
            
            # Verification checks
            print("\n4. VERIFICATION CHECKS")
            print("-" * 40)
            
            # Check all TOPICs have DESCRIPTIONs
            result = session.run("""
                MATCH (t:TOPIC)
                WHERE NOT (t)-[:HAS_DESCRIPTION]->(:DESCRIPTION)
                RETURN count(t) as count
            """)
            topics_without_desc = result.single()["count"]
            report["verification_checks"]["topics_without_description"] = topics_without_desc
            print(f"   TOPICs without DESCRIPTION: {topics_without_desc}")
            
            # Check all TOPICs with parents have HAS_CHILD relationship
            result = session.run("""
                MATCH (t:TOPIC)
                WHERE t.parent IS NOT NULL 
                AND t.parent <> 'no parent'
                AND NOT (:TOPIC)-[:HAS_CHILD]->(t)
                RETURN count(t) as count
            """)
            topics_without_parent_rel = result.single()["count"]
            report["verification_checks"]["topics_without_parent_rel"] = topics_without_parent_rel
            print(f"   TOPICs without parent relationship: {topics_without_parent_rel}")
            
            # Verify specific new topics exist
            print("\n5. NEW TOPICS VERIFICATION")
            print("-" * 40)
            new_topics = [
                "topic.NULL TOPIC",
                "topic.APOCALYPSE", 
                "topic.BEAUTY",
                "topic.ECONOMICS",
                "topic.ENTITLEMENT",
                "topic.EVANGELISM",
                "topic.FIN GOV",
                "topic.POLITICAL SCIENCE",
                "topic.THE BIBLE"
            ]
            
            all_present = True
            for topic_name in new_topics:
                result = session.run(
                    "MATCH (t:TOPIC {name: $name}) RETURN t.name as name",
                    name=topic_name
                )
                exists = result.single()
                status = "✓" if exists else "✗ MISSING"
                print(f"   {status} {topic_name}")
                if not exists:
                    all_present = False
            
            report["verification_checks"]["all_new_topics_present"] = all_present
            
            # Sample data verification
            print("\n6. SAMPLE DATA VERIFICATION")
            print("-" * 40)
            
            # Check a specific topic
            result = session.run("""
                MATCH (t:TOPIC {name: "topic.THE BIBLE"})
                RETURN t.name as name, t.alias as alias, t.level as level
            """)
            record = result.single()
            if record:
                print(f"   Sample: {record['name']}")
                print(f"     alias: {record['alias']}")
                print(f"     level: {record['level']}")
            
            # Check its description
            result = session.run("""
                MATCH (t:TOPIC {name: "topic.THE BIBLE"})-[:HAS_DESCRIPTION]->(d:DESCRIPTION)
                RETURN d.en_title as title, d.name as desc_name
            """)
            record = result.single()
            if record:
                print(f"     description: {record['desc_name']}")
                print(f"     en_title: {record['title']}")
        
        # Save final report
        report_path = REPORT_DIR / f"FINAL_SYNC_REPORT_{TIMESTAMP}.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "=" * 80)
        print("SYNCHRONIZATION COMPLETE")
        print("=" * 80)
        print(f"\nFinal report saved to: {report_path}")
        
        return report
        
    finally:
        driver.close()

if __name__ == "__main__":
    generate_final_report()
