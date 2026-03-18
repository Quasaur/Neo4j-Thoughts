---
type: THOUGHT
name: "thought.UNIVERSE INSIDE GOD"
alias: "Thought: Universe Inside God"
parent: "topic.THE GODHEAD"
en_content: "You do know that all of us--yeah, the entire Universe--is inside of God, right? Jeremiah 23:24"
tags: ["universe", "god", "presence", "infinity", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013e)
CREATE (t:THOUGHT {    name: "thought.UNIVERSE INSIDE GOD",
    alias: "Thought: Universe Inside God",
    parent: "topic.THE GODHEAD",
    tags: ['universe', 'god', 'presence', 'infinity', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.UNIVERSE INSIDE GOD",
    ctype: "THOUGHT",
    en_title: "Universe Inside God",
    en_content: "You do know that all of us--yeah, the entire Universe--is inside of God, right? Jeremiah 23:24",
    es_title: "El Universo Dentro de Dios",
    es_content: "¿Sabes que todos nosotros--sí, todo el Universo--está dentro de Dios, verdad? Jeremías 23:24",
    fr_title: "L'Univers à l'Intérieur de Dieu",
    fr_content: "Tu sais que nous tous--oui, tout l'Univers--sommes à l'intérieur de Dieu, n'est-ce pas ? Jérémie 23:24",
    hi_title: "परमेश्वर के भीतर ब्रह्मांड",
    hi_content: "आप जानते हैं कि हम सभी--हाँ, संपूर्ण ब्रह्मांड--परमेश्वर के भीतर है, सही? यिर्मयाह 23:24",
    zh_title: "Yuzhouji zai Shen li",
    zh_content: "Ni zhidao women suoyou ren--dui, zhengge yuzhou--dou zai Shen limian, duiba? Yelimishu 23:24"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNIVERSE INSIDE GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->UNIVERSE INSIDE GOD"
RETURN t, parent;
```
