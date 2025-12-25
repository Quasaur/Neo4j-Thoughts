```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.MOTION'
SET c.ctype = 1;
```