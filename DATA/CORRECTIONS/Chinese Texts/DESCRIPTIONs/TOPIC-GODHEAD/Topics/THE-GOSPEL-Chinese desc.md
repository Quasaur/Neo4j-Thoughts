```Cypher
MATCH (n {en_title: "THE GOSPEL"})
SET n.zh_title = 'Fúyīn'
SET n.zh_content = "yēsū jīdū de shēngpíng, sǐwáng, máizàng, fùhuó, shēngtiān hé zàilái.";
```