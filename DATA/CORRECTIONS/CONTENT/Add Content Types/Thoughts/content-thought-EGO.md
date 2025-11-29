```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.EGO'
SET c.ctype = 1;
```