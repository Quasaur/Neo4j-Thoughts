---
type: THOUGHT
name: "thought.TREASURE UNDER GARBAGE"
alias: "Thought: Treasure Under Garbage"
parent: "topic.WISDOM"
en_content: "Treasure is often hidden under garbage...be a treasure hunter!"
tags: ["wisdom", "treasure", "perspective", "search", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012c)
CREATE (t:THOUGHT {    name: "thought.TREASURE UNDER GARBAGE",
    alias: "Thought: Treasure Under Garbage",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'treasure', 'perspective', 'search', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.TREASURE UNDER GARBAGE",
    ctype: "THOUGHT",
    en_title: "Treasure Under Garbage",
    en_content: "Treasure is often hidden under garbage...be a treasure hunter!",
    es_title: "Tesoro Bajo la Basura",
    es_content: "El tesoro a menudo se esconde bajo la basura...¡sé un cazador de tesoros!",
    fr_title: "Trésor Sous les Déchets",
    fr_content: "Le trésor est souvent caché sous les déchets...soyez un chasseur de trésors !",
    hi_title: "कचरे के नीचे खजाना",
    hi_content: "खजाना अक्सर कचरे के नीचे छुपा होता है...खजाने का शिकारी बनो!",
    zh_title: "La Ji Xia De Bao Zang",
    zh_content: "Bao zang chang chang yin cang zai la ji xia...zuo yi ge bao zang lie ren!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TREASURE UNDER GARBAGE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->TREASURE UNDER GARBAGE"
RETURN t, parent;
```
