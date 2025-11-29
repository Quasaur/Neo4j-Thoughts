the DESCRIPTION  'desc.TRUTH' is errantly named 'desc.THE GOSPEL'...
...this is the correction
```Cypher
MATCH (n {en_title: "TRUTH"})
SET n.name = "desc.TRUTH";
```