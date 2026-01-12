---
name: "thought.EVIL NO CHANCE"
alias: "Thought: Evil No Chance"
type: THOUGHT
en_content: "Look at God. Evil never had a chance!"
parent: "topic.THE GODHEAD"
tags:
- god
- evil
- victory
- majesty
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.EVIL NO CHANCE",
    alias: "Thought: Evil No Chance",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'evil', 'victory', 'majesty', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EVIL NO CHANCE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVIL NO CHANCE" AND c.name = "content.EVIL NO CHANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVIL NO CHANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EVIL NO CHANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EVIL NO CHANCE" }]->(child);
```
