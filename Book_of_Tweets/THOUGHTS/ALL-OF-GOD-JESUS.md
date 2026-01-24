---
name: "thought.ALL OF GOD JESUS"
alias: "Thought: All Of God Jesus"
type: THOUGHT
en_content: "Jesus Christ is the only Man Who could fit ALL OF GOD in Himself, because HE IS GOD!"
parent: topic.THE GOSPEL
tags:
  - jesus
  - christ
  - fullness
  - divinity
  - god
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.ALL OF GOD JESUS",
    alias: "Thought: All Of God Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'christ', 'fullness', 'divinity', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ALL OF GOD JESUS",
    en_title: "All Of God Jesus",
    en_content: "Jesus Christ is the only Man Who could fit ALL OF GOD in Himself, because HE IS GOD!",
    es_title: "Todo Dios en Jesús",
    es_content: "¡Jesucristo es el único Hombre que pudo contener TODO DE DIOS en Sí mismo, porque ÉL ES DIOS!",
    fr_title: "Tout Dieu en Jésus",
    fr_content: "Jésus-Christ est le seul Homme qui pourrait contenir TOUT DIEU en Lui-même, parce qu'IL EST DIEU !",
    hi_title: "यीशु में संपूर्ण परमेश्वर",
    hi_content: "यीशु मसीह एकमात्र मनुष्य हैं जो अपने आप में संपूर्ण परमेश्वर को समा सकते हैं, क्योंकि वे ही परमेश्वर हैं!",
    zh_title: "Yēsū shì shén",
    zh_content: "Yēsū jīdū shì wéiyī nénggòu jiāng quánbù de shén róngnà zài zìjǐ lǐmiàn de rén, yīnwèi tā jiùshì shén!"
});

MATCH (t:THOUGHT {name: "thought.ALL OF GOD JESUS"})
MATCH (c:CONTENT {name: "content.ALL OF GOD JESUS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALL OF GOD JESUS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.ALL OF GOD JESUS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->ALL OF GOD JESUS" }]->(child);
```
