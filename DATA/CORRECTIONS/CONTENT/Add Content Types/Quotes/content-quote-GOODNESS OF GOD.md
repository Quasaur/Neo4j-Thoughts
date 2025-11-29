```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.GOODNESS OF GOD'
SET c.ctype = 2;
```