```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.IMPERSONAL GOD'
SET c.ctype = 1;
```