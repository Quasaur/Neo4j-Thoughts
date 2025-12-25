```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.PROTECTION'
SET c.ctype = 1;
```