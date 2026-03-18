---
type: THOUGHT
name: "thought.ETERNAL GRACE MERCY"
alias: "Thought: Eternal Grace Mercy"
parent: "topic.THE GODHEAD"
en_content: "Psalm 136: Grace, Mercy and Kindness will never be obsolete; they endure forever."
tags: ["grace", "mercy", "kindness", "eternity", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.ETERNAL GRACE MERCY",
    alias: "Thought: Eternal Grace Mercy",
    parent: "topic.THE GODHEAD",
    tags: ['grace', 'mercy', 'kindness', 'eternity', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.ETERNAL GRACE MERCY",
    ctype: "THOUGHT",
    en_title: "Eternal Grace Mercy",
    en_content: "Psalm 136: Grace, Mercy and Kindness will never be obsolete; they endure forever.",
    es_title: "Gracia Eterna y Misericordia",
    es_content: "Salmo 136: La Gracia, la Misericordia y la Bondad nunca quedarán obsoletas; perduran para siempre.",
    fr_title: "Grâce Éternelle et Miséricorde",
    fr_content: "Psaume 136: La Grâce, la Miséricorde et la Bonté ne seront jamais obsolètes; elles durent éternellement.",
    hi_title: "शाश्वत अनुग्रह दया",
    hi_content: "भजन संहिता 136: अनुग्रह, दया और कृपा कभी भी अप्रचलित नहीं होंगे; वे सदा के लिए बने रहते हैं।",
    zh_title: "Yong heng en dian ci bei",
    zh_content: "Shi pian 136: En dian, ci bei he shan liang yong yuan bu hui guo shi; ta men cun dao yong yuan."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ETERNAL GRACE MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->ETERNAL GRACE MERCY"
RETURN t, parent;
```
