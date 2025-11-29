```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.THE ULTIMATE'
SET c.ctype = 1;
```