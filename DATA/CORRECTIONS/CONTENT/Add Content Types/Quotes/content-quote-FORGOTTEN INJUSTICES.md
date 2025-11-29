```Cypher
// find the content node
MATCH (c:CONTENT) WHERE c.name = 'content.FORGOTTEN INJUSTICES'
SET c.ctype = 2;
```