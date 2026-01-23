In the Neo4j Cypher language create an edge with the label "HAS_DESCRIPTION" and link it to two existing nodes, the first of which has the name property "NULL TOPIC" and the second of which has the name property "desc.NULL_TOPIC". The MATCH statement must have a RETURN clause.

To create an edge with the label `HAS_DESCRIPTION` in Neo4j's Cypher language, linking two nodes with the specified name properties, you can use the following query:

```cypher
MATCH (a {name: "NULL TOPIC"}), (b {name: "desc.NULL_TOPIC"})
RETURN a, b;
CREATE (a)-[:HAS_DESCRIPTION]->(b);
```

This query does the following:
1. It matches the first node `a` with the name property `"NULL TOPIC"`.
2. It matches the second node `b` with the name property `"desc.NULL_TOPIC"`.
3. It creates a directed relationship `HAS_DESCRIPTION` from node `a` to node `b`.