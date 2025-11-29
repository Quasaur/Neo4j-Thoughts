```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.THE ULTIMATE (2)'
SET c.ctype = 1;
```