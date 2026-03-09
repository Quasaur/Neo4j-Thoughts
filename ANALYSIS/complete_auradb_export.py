#!/usr/bin/env python3
"""
Complete Neo4j AuraDB Export (Schema + Data)
Exports all schema (indexes, constraints) and all graph data (nodes, relationships)
Uses native Cypher only - works on all Neo4j instances including AuraDB

Output: BACKUPS/auradb_complete_export_YYYYMMDD_HHMMSS.json
"""

import json
import os
from neo4j import GraphDatabase
from datetime import datetime
from pathlib import Path

# Neo4j AuraDB Connection
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Backup directory
BACKUP_DIR = Path("/Users/quasaur/Developer/Neo4j-Thoughts/BACKUPS")

def full_export():
    """Export complete database schema and data"""
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    timestamp = datetime.now()
    export_data = {
        "metadata": {
            "timestamp": timestamp.isoformat(),
            "date": timestamp.strftime("%Y-%m-%d"),
            "time": timestamp.strftime("%H:%M:%S"),
            "source": "Neo4j AuraDB",
            "uri": URI,
            "database": "neo4j"
        },
        "schema": {
            "indexes": [],
            "constraints": []
        },
        "summary": {
            "node_counts": {},
            "relationship_counts": {}
        },
        "nodes": {},
        "relationships": []
    }
    
    try:
        print("=" * 80)
        print("COMPLETE AURADB EXPORT - SCHEMA + DATA")
        print("=" * 80)
        print(f"Started: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        with driver.session() as session:
            
            # 1. CAPTURE INDEXES
            print("[1/5] Exporting indexes...")
            try:
                result = session.run("SHOW INDEXES")
                for record in result:
                    index_data = {key: record.get(key) for key in record.keys()}
                    export_data["schema"]["indexes"].append(index_data)
                print(f"       ✓ Found {len(export_data['schema']['indexes'])} indexes")
            except Exception as e:
                print(f"       ⚠ Could not export indexes: {e}")
            
            # 2. CAPTURE CONSTRAINTS
            print("[2/5] Exporting constraints...")
            try:
                result = session.run("SHOW CONSTRAINTS")
                for record in result:
                    constraint_data = {key: record.get(key) for key in record.keys()}
                    export_data["schema"]["constraints"].append(constraint_data)
                print(f"       ✓ Found {len(export_data['schema']['constraints'])} constraints")
            except Exception as e:
                print(f"       ⚠ Could not export constraints: {e}")
            
            # 3. DISCOVER ALL LABELS
            print("[3/5] Discovering node labels...")
            result = session.run("""
                CALL db.labels() YIELD label
                RETURN collect(label) as labels
            """)
            labels = result.single()["labels"]
            print(f"       ✓ Found {len(labels)} labels: {', '.join(labels)}")
            
            # 4. CAPTURE ALL NODE DATA
            print("[4/5] Exporting nodes...")
            total_nodes = 0
            
            for label in labels:
                result = session.run(f"""
                    MATCH (n:{label})
                    RETURN n.name as name, 
                           n.title as title,
                           labels(n) as labels,
                           properties(n) as props
                """)
                
                nodes = []
                for record in result:
                    node_data = {
                        "labels": record["labels"],
                        "properties": dict(record["props"])
                    }
                    # Add identifier for relationships
                    if record["name"]:
                        node_data["_identifier"] = record["name"]
                    elif record["title"]:
                        node_data["_identifier"] = record["title"]
                    else:
                        # Generate identifier from properties
                        props = record["props"]
                        node_data["_identifier"] = f"{label}_{id(props)}"
                    
                    nodes.append(node_data)
                
                export_data["nodes"][label] = nodes
                export_data["summary"]["node_counts"][label] = len(nodes)
                total_nodes += len(nodes)
                print(f"       ✓ {label}: {len(nodes)} nodes")
            
            print(f"       Total nodes: {total_nodes}")
            
            # 5. CAPTURE ALL RELATIONSHIPS
            print("[5/5] Exporting relationships...")
            result = session.run("""
                MATCH (a)-[r]->(b)
                RETURN type(r) as rel_type,
                       labels(a)[0] as from_label,
                       a.name as from_name,
                       labels(b)[0] as to_label,
                       b.name as to_name,
                       properties(r) as props
                ORDER BY rel_type
            """)
            
            rel_types = set()
            for record in result:
                rel_data = {
                    "type": record["rel_type"],
                    "from": {
                        "label": record["from_label"],
                        "name": record["from_name"]
                    },
                    "to": {
                        "label": record["to_label"],
                        "name": record["to_name"]
                    },
                    "properties": dict(record["props"])
                }
                export_data["relationships"].append(rel_data)
                rel_types.add(record["rel_type"])
            
            # Count relationships by type
            for rel_type in rel_types:
                count = sum(1 for r in export_data["relationships"] if r["type"] == rel_type)
                export_data["summary"]["relationship_counts"][rel_type] = count
            
            print(f"       ✓ Found {len(export_data['relationships'])} relationships")
            print(f"         Types: {', '.join(sorted(rel_types))}")
        
        # Save to file with timestamp
        filename = f"auradb_complete_export_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        filepath = BACKUP_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        # Get file size
        file_size = os.path.getsize(filepath)
        file_size_mb = file_size / (1024 * 1024)
        
        print()
        print("=" * 80)
        print("EXPORT COMPLETE")
        print("=" * 80)
        print(f"File: {filepath}")
        print(f"Size: {file_size_mb:.2f} MB")
        print()
        print("Summary:")
        print(f"  Indexes: {len(export_data['schema']['indexes'])}")
        print(f"  Constraints: {len(export_data['schema']['constraints'])}")
        print(f"  Node labels: {len(labels)}")
        print(f"  Total nodes: {total_nodes}")
        print(f"  Total relationships: {len(export_data['relationships'])}")
        print(f"  Relationship types: {len(rel_types)}")
        print()
        
        return filepath, export_data
        
    except Exception as e:
        print(f"\n❌ EXPORT FAILED: {e}")
        raise
        
    finally:
        driver.close()


def verify_backup(backup_file):
    """Verify the backup file is valid JSON and contains expected structure"""
    print(f"\nVerifying backup: {backup_file}")
    
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        checks = [
            ("metadata" in data, "metadata section"),
            ("schema" in data, "schema section"),
            ("nodes" in data, "nodes section"),
            ("relationships" in data, "relationships section"),
            ("indexes" in data["schema"], "indexes in schema"),
            ("constraints" in data["schema"], "constraints in schema"),
        ]
        
        print("\nVerification checks:")
        for passed, check_name in checks:
            status = "✓" if passed else "✗"
            print(f"  {status} {check_name}")
        
        all_passed = all(c[0] for c in checks)
        
        if all_passed:
            print("\n✅ Backup file is valid!")
        else:
            print("\n⚠ Backup file may be incomplete")
        
        return all_passed
        
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Verification error: {e}")
        return False


if __name__ == "__main__":
    # Ensure backup directory exists
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    
    # Perform export
    filepath, data = full_export()
    
    # Verify the backup
    verify_backup(filepath)
    
    print(f"\nBackup location: {filepath}")
