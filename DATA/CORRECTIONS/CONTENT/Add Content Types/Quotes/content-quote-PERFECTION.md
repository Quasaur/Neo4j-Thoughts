```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.PERFECTION'
SET c.ctype = 2;
```