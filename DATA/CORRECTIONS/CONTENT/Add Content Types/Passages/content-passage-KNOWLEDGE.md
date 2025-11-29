```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.KNOWLEDGE'
SET c.ctype = 3;
```