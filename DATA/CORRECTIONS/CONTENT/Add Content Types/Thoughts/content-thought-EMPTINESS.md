```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.EMPTINESS'
SET c.ctype = 1;
```