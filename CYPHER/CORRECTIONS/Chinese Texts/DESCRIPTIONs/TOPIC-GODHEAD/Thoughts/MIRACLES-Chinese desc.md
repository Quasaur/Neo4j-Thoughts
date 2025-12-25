```Cypher
MATCH (n {en_title: "MIRACLES"})
SET n.zh_title = 'Qíjì'
SET n.zh_content = "qíjì shì……
……shì shàngdì céngjīng zuòguò de wéiyī shìjì,
shì shàngdì zhèngzài zuò de wéiyī shìjì,
yěshì shàngdì jiānglái yào zuò de wéiyī shìjì!";
```