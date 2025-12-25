```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.MIRACLES (2)'
SET c.ctype = 2;
```