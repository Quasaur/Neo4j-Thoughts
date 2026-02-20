#!/usr/bin/env python3
"""
Check Neo4j AuraDB for duplicate nodes across all labels.
Reports duplicates based on the 'name' property which should be unique.
"""

from neo4j import GraphDatabase

URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")


def check_duplicates():
    """Check for duplicate nodes across all labels."""
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            print("=" * 80)
            print("Neo4j AuraDB Duplicate Node Checker")
            print("=" * 80)
            
            # Query to find all nodes with duplicate names grouped by label
            query = """
            MATCH (n)
            WHERE n.name IS NOT NULL
            WITH labels(n) as node_labels, n.name as name, count(*) as count
            WHERE count > 1
            RETURN node_labels, name, count
            ORDER BY count DESC, name
            """
            
            result = session.run(query)
            duplicates = list(result)
            
            if not duplicates:
                print("\n✅ No duplicate nodes found!")
                print("\nAll nodes have unique 'name' property values.")
                return
            
            print(f"\n⚠️  FOUND {len(duplicates)} DUPLICATE NAME(S):\n")
            print("-" * 80)
            
            for record in duplicates:
                labels = record["node_labels"]
                name = record["name"]
                count = record["count"]
                label_str = ":".join(labels) if labels else "(no label)"
                
                print(f"\n{label_str} | '{name}'")
                print(f"  Count: {count} nodes")
                
                # Get details of each duplicate node
                detail_query = """
                MATCH (n {name: $name})
                RETURN id(n) as node_id, elementId(n) as element_id, 
                       labels(n) as labels, properties(n) as props
                ORDER BY id(n)
                """
                detail_result = session.run(detail_query, name=name)
                
                for idx, node_record in enumerate(detail_result, 1):
                    node_id = node_record["node_id"]
                    element_id = node_record["element_id"]
                    props = node_record["props"]
                    
                    print(f"\n  Node #{idx}:")
                    print(f"    Internal ID: {node_id}")
                    print(f"    Element ID: {element_id}")
                    
                    # Show key properties (excluding name which we already know)
                    other_props = {k: v for k, v in props.items() if k != "name"}
                    if other_props:
                        print(f"    Properties:")
                        for key, value in sorted(other_props.items())[:5]:  # Limit to 5 props
                            value_str = str(value)[:60]
                            if len(str(value)) > 60:
                                value_str += "..."
                            print(f"      {key}: {value_str}")
                    
                    # Check for relationships
                    rel_query = """
                    MATCH (n {name: $name})
                    WHERE id(n) = $node_id
                    OPTIONAL MATCH (n)-[r]-(other)
                    RETURN type(r) as rel_type, 
                           case when startNode(r) = n then 'OUT' else 'IN' end as direction,
                           labels(other) as other_labels, 
                           other.name as other_name
                    LIMIT 10
                    """
                    rel_result = session.run(rel_query, name=name, node_id=node_id)
                    relationships = list(rel_result)
                    
                    has_rels = any(r["rel_type"] for r in relationships)
                    if has_rels:
                        print(f"    Relationships:")
                        for rel in relationships:
                            if rel["rel_type"]:
                                other_label = rel["other_labels"][0] if rel["other_labels"] else "?"
                                other_name = rel["other_name"] or f"ID:{rel['other_id']}"
                                arrow = "->" if rel["direction"] == "OUT" else "<-"
                                print(f"      {arrow} [: {rel['rel_type']} ] {other_label} '{other_name}'")
                    else:
                        print(f"    Relationships: None")
                
                print("\n  " + "-" * 76)
            
            # Summary by label
            print("\n" + "=" * 80)
            print("SUMMARY BY LABEL")
            print("=" * 80)
            
            summary_query = """
            MATCH (n)
            WHERE n.name IS NOT NULL
            WITH labels(n) as node_labels, n.name as name, count(*) as count
            WHERE count > 1
            WITH node_labels, count(*) as duplicate_names, sum(count) as total_duplicate_nodes
            RETURN node_labels, duplicate_names, total_duplicate_nodes
            ORDER BY total_duplicate_nodes DESC
            """
            
            summary_result = session.run(summary_query)
            
            print(f"\n{'Label':<30} {'Duplicate Names':<20} {'Total Nodes':<15}")
            print("-" * 65)
            
            for record in summary_result:
                labels = record["node_labels"]
                dup_names = record["duplicate_names"]
                total_nodes = record["total_duplicate_nodes"]
                label_str = ":".join(labels) if labels else "(no label)"
                print(f"{label_str:<30} {dup_names:<20} {total_nodes:<15}")
            
            # Recommendations
            print("\n" + "=" * 80)
            print("RECOMMENDATIONS")
            print("=" * 80)
            print("""
1. Review duplicate nodes above and identify which to keep
2. For each duplicate set, decide which node has correct relationships
3. Delete duplicate nodes using DETACH DELETE
4. Consider adding uniqueness constraints:
   
   CREATE CONSTRAINT thought_name_unique IF NOT EXISTS
   FOR (t:THOUGHT) REQUIRE t.name IS UNIQUE;
   
   CREATE CONSTRAINT content_name_unique IF NOT EXISTS
   FOR (c:CONTENT) REQUIRE c.name IS UNIQUE;
""")
            
    finally:
        driver.close()


if __name__ == "__main__":
    check_duplicates()
