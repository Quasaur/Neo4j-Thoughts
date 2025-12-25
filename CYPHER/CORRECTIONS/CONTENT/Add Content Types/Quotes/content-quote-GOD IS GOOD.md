```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.GOD IS GOOD'
SET c.ctype = 2;
```