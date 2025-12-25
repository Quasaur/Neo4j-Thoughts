```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.GOD-AWARENESS'
SET c.ctype = 1;
```