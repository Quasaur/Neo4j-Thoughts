```Cypher
MATCH (n {en_title: "THE HOLY SPIRIT"})
SET n.zh_title = 'Shènglíng'
SET n.zh_content = "shènglíng shì shén, suǒyǒu de rén dōu bìxū bèi tā chōngmǎn.";
```