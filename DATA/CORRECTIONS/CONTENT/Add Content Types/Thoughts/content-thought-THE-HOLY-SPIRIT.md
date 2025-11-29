```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.THE HOLY SPIRIT'
SET c.ctype = 1;
```