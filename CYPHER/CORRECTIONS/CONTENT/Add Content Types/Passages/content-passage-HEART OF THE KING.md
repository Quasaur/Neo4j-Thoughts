```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.HEART OF THE KING'
SET c.ctype = 3;
```