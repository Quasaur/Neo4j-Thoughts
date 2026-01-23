---
name: "thought.CHRIST UNIVERSAL DESTINY"
alias: "Thought: Christ Universal Destiny"
type: THOUGHT
en_content: "Christ is everyone's Destiny...no exceptions!"
parent: "topic.THE GODHEAD"
tags:
- christ
- destiny
- eternity
- divinity
- hope
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2012b)
CREATE (t:THOUGHT {
    name: "thought.CHRIST UNIVERSAL DESTINY",
    alias: "Thought: Christ Universal Destiny",
    parent: "topic.THE GODHEAD",
    tags: ['christ', 'destiny', 'eternity', 'divinity', 'hope'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHRIST UNIVERSAL DESTINY",
    en_title: "Christ Universal Destiny",
    en_content: "Christ is everyone's Destiny...no exceptions!",
    es_title: "Cristo es el Destino Universal",
    es_content: "¡Cristo es el Destino de todos... sin excepciones!",
    fr_title: "Le Christ est la Destinée Universelle",
    fr_content: "Le Christ est la Destinée de tous... sans exception !",
    hi_title: "मसीह सार्वभौमिक नियति है",
    hi_content: "मसीह सभी की नियति है... कोई अपवाद नहीं!",
    zh_title: "Jīdū shì pǔshì de mìngyùn 基督是普世的命运",
    zh_content: "Jīdū shì měi gèrén de mìngyùn... méiyǒu lìwài! 基督是每个人的命运...没有例外！"
});

MATCH (t:THOUGHT {name: "thought.CHRIST UNIVERSAL DESTINY"})
MATCH (c:CONTENT {name: "content.CHRIST UNIVERSAL DESTINY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRIST UNIVERSAL DESTINY" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.CHRIST UNIVERSAL DESTINY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHRIST UNIVERSAL DESTINY" }]->(child);
```
