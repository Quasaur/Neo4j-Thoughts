---
type: THOUGHT
name: "thought.HELL FIRE FOR DEVIL"
alias: "Thought: Hell Fire For Devil"
parent: "topic.THE GODHEAD"
en_content: "Hell Fire wasn't made by the Devil...it was made for the Devil by God."
tags: ["hell", "devil", "god", "judgment", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Aug-2013)
CREATE (t:THOUGHT {    name: "thought.HELL FIRE FOR DEVIL",
    alias: "Thought: Hell Fire For Devil",
    parent: "topic.THE GODHEAD",
    tags: ['hell', 'devil', 'god', 'judgment', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.HELL FIRE FOR DEVIL",
    ctype: "THOUGHT",
    en_title: "Hell Fire For Devil",
    en_content: "Hell Fire wasn't made by the Devil...it was made for the Devil by God.",
    es_title: "Fuego del Infierno Para el Diablo",
    es_content: "El Fuego del Infierno no fue hecho por el Diablo...fue hecho para el Diablo por Dios.",
    fr_title: "Le Feu de l'Enfer Pour le Diable",
    fr_content: "Le Feu de l'Enfer n'a pas été créé par le Diable...il a été créé pour le Diable par Dieu.",
    hi_title: "शैतान के लिए नरक की आग",
    hi_content: "नरक की आग शैतान द्वारा नहीं बनाई गई थी...यह परमेश्वर द्वारा शैतान के लिए बनाई गई थी।",
    zh_title: "Wei Mo Gui De Di Yu Zhi Huo",
    zh_content: "Di Yu Zhi Huo Bu Shi Mo Gui Zao De...Shi Shang Di Wei Mo Gui Zao De."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HELL FIRE FOR DEVIL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->HELL FIRE FOR DEVIL"
RETURN t, parent;
```
