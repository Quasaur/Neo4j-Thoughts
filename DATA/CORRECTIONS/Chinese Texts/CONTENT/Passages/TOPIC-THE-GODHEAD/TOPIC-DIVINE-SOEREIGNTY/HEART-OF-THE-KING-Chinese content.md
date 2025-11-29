```Cypher
MATCH (c:CONTENT {en_title: "HEART OF THE KING"})
SET c.zh_title = 'Wáng de xīn'
SET c.zh_content = "wáng de xīn zài yēhéhuá shǒuzhōng hǎoxiàng gōuqú de shuǐ, tā kěyǐ suíyì liúzhuàn.";
```