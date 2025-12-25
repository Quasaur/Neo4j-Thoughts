```Cypher
MATCH (n)
WHERE elementId(n) = "your_element_id"
DETACH DELETE n;
```