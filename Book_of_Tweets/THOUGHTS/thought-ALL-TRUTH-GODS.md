---
type: THOUGHT
name: "thought.ALL TRUTH GODS"
alias: "Thought: All Truth Gods"
parent: "topic.TRUTH"
en_content: "All truth belongs to God."
tags: ["truth", "ownership", "god", "revelation", "philosophy"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Feb-2013)
CREATE (t:THOUGHT {    name: "thought.ALL TRUTH GODS",
    alias: "Thought: All Truth Gods",
    parent: "topic.TRUTH",
    tags: ['truth', 'ownership', 'god', 'revelation', 'philosophy'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.ALL TRUTH GODS",
    ctype: "THOUGHT",
    en_title: "All Truth Gods",
    en_content: "All truth belongs to God.",
    es_title: "Toda Verdad es de Dios",
    es_content: "Toda verdad pertenece a Dios.",
    fr_title: "Toute Vérité Appartient à Dieu",
    fr_content: "Toute vérité appartient à Dieu.",
    hi_title: "सभी सत्य परमेश्वर के हैं",
    hi_content: "सभी सत्य परमेश्वर के हैं।",
    zh_title: "Zhēnlǐ shǔyú shén",
    zh_content: "Yīqiè zhēnlǐ dōu shǔyú shén."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ALL TRUTH GODS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->ALL TRUTH GODS"
RETURN t, parent;
```
