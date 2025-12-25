```Cypher
MATCH (n) WHERE n.tags IS NOT NULL RETURN n.tags AS allTags;
```

with Node Name:

```Cypher
MATCH (n)
WHERE n.tags IS NOT NULL
RETURN n.name as Node, n.tags AS allTags;
```