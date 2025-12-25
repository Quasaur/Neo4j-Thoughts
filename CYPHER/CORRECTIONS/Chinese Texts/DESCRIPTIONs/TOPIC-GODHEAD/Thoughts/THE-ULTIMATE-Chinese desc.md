```Cypher
MATCH (n {en_title: "THE ULTIMATE"})
SET n.zh_title = 'Zhōngjí'
SET n.zh_content = "chúfēi 'tā'(tā) yě jùyǒu wèi gé xìng, fǒuzé zhōngjí zhī wù bù kěnéng shì zhōngjí.";
```