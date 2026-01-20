---
name: "thought.ARROGANCE VS DIGNITY"
alias: "Thought: Arrogance Vs Dignity"
type: THOUGHT
en_content: "Far too many black men have mistaken arrogance for dignity."
parent: "topic.HUMANITY"
tags:
- dignity
- arrogance
- humanity
- character
- race
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.ARROGANCE VS DIGNITY",
    alias: "Thought: Arrogance Vs Dignity",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'arrogance', 'humanity', 'character', 'race'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ARROGANCE VS DIGNITY",
    en_title: "Arrogance Vs Dignity",
    en_content: "Far too many black men have mistaken arrogance for dignity.",
    es_title: "Arrogancia vs Dignidad",
    es_content: "Demasiados hombres negros han confundido la arrogancia con la dignidad.",
    fr_title: "Arrogance vs Dignité",
    fr_content: "Beaucoup trop d'hommes noirs ont confondu l'arrogance avec la dignité.",
    hi_title: "अहंकार बनाम गरिमा",
    hi_content: "बहुत से अश्वेत पुरुषों ने अहंकार को गरिमा समझ लिया है।",
    zh_title: "Àomàn yǔ zūnyán",
    zh_content: "Tài duō hēirén nánxìng jiāng àomàn wù rènwéi shì zūnyán."
});

MATCH (t:THOUGHT {name: "thought.ARROGANCE VS DIGNITY"})
MATCH (c:CONTENT {name: "content.ARROGANCE VS DIGNITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ARROGANCE VS DIGNITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.ARROGANCE VS DIGNITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >ARROGANCE VS DIGNITY" }]->(child);
```
