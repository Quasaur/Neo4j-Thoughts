---
type: THOUGHT
name: "thought.EVIL NO CHANCE"
alias: "Thought: Evil No Chance"
parent: "topic.THE GODHEAD"
en_content: "Look at God. Evil never had a chance!"
tags: ["god", "evil", "victory", "majesty", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013b)
CREATE (t:THOUGHT {    name: "thought.EVIL NO CHANCE",
    alias: "Thought: Evil No Chance",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'evil', 'victory', 'majesty', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.EVIL NO CHANCE",
    ctype: "THOUGHT",
    en_title: "Evil No Chance",
    en_content: "Look at God. Evil never had a chance!",
    es_title: "El Mal Sin Oportunidad",
    es_content: "¡Mira a Dios. El mal nunca tuvo oportunidad!",
    fr_title: "Le Mal Sans Chance",
    fr_content: "Regardez Dieu. Le mal n'a jamais eu une chance !",
    hi_title: "बुराई का कोई अवसर नहीं",
    hi_content: "परमेश्वर को देखिए। बुराई का कभी कोई अवसर ही नहीं था!",
    zh_title: "È Méi Yǒu Jī Huì",
    zh_content: "Kàn Shàng Dì. È cóng lái méi yǒu jī huì!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVIL NO CHANCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->EVIL NO CHANCE"
RETURN t, parent;
```
