```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.ETERNITY'
SET c.ctype = 2;
```