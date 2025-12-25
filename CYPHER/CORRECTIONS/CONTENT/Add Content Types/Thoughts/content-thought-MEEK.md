```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.MEEK'
SET c.ctype = 1;
```