---
name: "thought.NOBODY LOVES LIKE JESUS"
alias: "Thought: Nobody Loves Like Jesus"
type: THOUGHT
en_content: "My mother loved me VERY MUCH; but on her finest day she could not take away my sins...nobody loves me like Jesus!"
parent: "topic.THE GODHEAD"
tags:
- love
- jesus
- salvation
- sin
- mother
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Jul-2011)
CREATE (t:THOUGHT {
    name: "thought.NOBODY LOVES LIKE JESUS",
    alias: "Thought: Nobody Loves Like Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'jesus', 'salvation', 'sin', 'mother'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOBODY LOVES LIKE JESUS",
    en_title: "Nobody Loves Like Jesus",
    en_content: "My mother loved me VERY MUCH; but on her finest day she could not take away my sins...nobody loves me like Jesus!",
    es_title: "Nadie Ama Como Jesús",
    es_content: "Mi madre me amaba MUCHO; pero en su mejor día no pudo quitar mis pecados... ¡nadie me ama como Jesús!",
    fr_title: "Personne n'Aime Comme Jésus",
    fr_content: "Ma mère m'aimait BEAUCOUP ; mais dans son meilleur jour, elle ne pouvait pas enlever mes péchés... personne ne m'aime comme Jésus !",
    hi_title: "कोई यीशु जैसा प्यार नहीं करता",
    hi_content: "मेरी माँ मुझसे बहुत प्यार करती थी; लेकिन अपने सबसे अच्छे दिन में भी वह मेरे पापों को दूर नहीं कर सकती थी... कोई भी मुझसे यीशु जैसा प्यार नहीं करता!",
    zh_title: "Méiyǒu rén xiàng Yēsū nàyàng ài wǒ 没有人像耶稣那样爱我",
    zh_content: "Wǒ de mǔqīn fēicháng ài wǒ; dàn zài tā zuì hǎo de rìzi lǐ, tā yě wúfǎ bā wǒ de zuìniè dài zǒu... méiyǒu rén xiàng Yēsū nàyàng ài wǒ! 我的母亲非常爱我；但在她最好的日子里，她也无法把我的罪孽带走...没有人像耶稣那样爱我！"
});

MATCH (t:THOUGHT {name: "thought.NOBODY LOVES LIKE JESUS"})
MATCH (c:CONTENT {name: "content.NOBODY LOVES LIKE JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOBODY LOVES LIKE JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.NOBODY LOVES LIKE JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->NOBODY LOVES LIKE JESUS" }]->(child);
```
