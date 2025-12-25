```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.MIRACLES'
SET c.ctype = 1;
```