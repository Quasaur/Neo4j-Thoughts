```Cypher
MATCH (c:CONTENT {en_title: "ETERNITY"})
SET c.zh_title = 'Yǒnghéng'
SET c.zh_content = "'yǒnghéng' yī cí yìwèizhe (zhìshǎo zài lǐzhì shàng) shàngdì wú shǐ, zhè gěi wǒmen zhèxiē miǎoxiǎo de xīnlíng dài láile gè zhǒng gè yàng de wèntí.";
```