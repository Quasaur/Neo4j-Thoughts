---
type: THOUGHT
name: "thought.CHRIST UNIVERSAL DESTINY"
alias: "Thought: Christ Universal Destiny"
parent: "topic.THE GODHEAD"
en_content: "Christ is everyone's Destiny...no exceptions!"
tags: ["christ", "destiny", "eternity", "divinity", "hope"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012b)
CREATE (t:THOUGHT {    name: "thought.CHRIST UNIVERSAL DESTINY",
    alias: "Thought: Christ Universal Destiny",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'destiny', 'eternity', 'divinity', 'hope'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.CHRIST UNIVERSAL DESTINY",
    ctype: "THOUGHT",
    en_title: "Christ Universal Destiny",
    en_content: "Christ is everyone's Destiny...no exceptions!",
    es_title: "Cristo es el Destino Universal",
    es_content: "¡Cristo es el Destino de todos... sin excepciones!",
    fr_title: "Le Christ est la Destinée Universelle",
    fr_content: "Le Christ est la Destinée de tous... sans exception !",
    hi_title: "मसीह सार्वभौमिक नियति है",
    hi_content: "मसीह सभी की नियति है... कोई अपवाद नहीं!",
    zh_title: "Jīdū shì pǔshì de mìngyùn  jī dū shì pǔ shì de mìng yùn",
    zh_content: "Jīdū shì měi gèrén de mìngyùn... méiyǒu lìwài!  jī dū shì měi gè rén de mìng yùn ... méi yǒu lì wài ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CHRIST UNIVERSAL DESTINY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->CHRIST UNIVERSAL DESTINY"
RETURN t, parent;
```
