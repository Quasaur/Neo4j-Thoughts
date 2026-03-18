---
type: THOUGHT
name: "thought.UNGRATEFUL HUMAN RACE"
alias: "Thought: Ungrateful Human Race"
parent: "topic.HUMANITY"
en_content: "What single word best describes the human race? UNGRATEFUL."
tags: ["ingratitude", "humanity", "character", "judgment", "truth"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Apr-2012)
CREATE (t:THOUGHT {    name: "thought.UNGRATEFUL HUMAN RACE",
    alias: "Thought: Ungrateful Human Race",
    parent: "topic.HUMANITY",
    tags: ['ingratitude', 'humanity', 'character', 'judgment', 'truth'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.UNGRATEFUL HUMAN RACE",
    ctype: "THOUGHT",
    en_title: "Ungrateful Human Race",
    en_content: "What single word best describes the human race? UNGRATEFUL.",
    es_title: "Raza Humana Ingrata",
    es_content: "¿Qué palabra describe mejor a la raza humana? INGRATA.",
    fr_title: "Race Humaine Ingrate",
    fr_content: "Quel mot unique décrit le mieux la race humaine ? INGRATE.",
    hi_title: "कृतघ्न मानव जाति",
    hi_content: "मानव जाति का सबसे अच्छा वर्णन कौन सा एक शब्द करता है? कृतघ्न।",
    zh_title: "Bu Gan En De Ren Lei",
    zh_content: "Shen Me Dan Ge Ci Zui Neng Miao Shu Ren Lei? Bu Gan En."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNGRATEFUL HUMAN RACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->UNGRATEFUL HUMAN RACE"
RETURN t, parent;
```
