---
name: "thought.UNGRATEFUL HUMAN RACE"
alias: "Thought: Ungrateful Human Race"
type: THOUGHT
en_content: "What single word best describes the human race? UNGRATEFUL."
parent: "topic.HUMANITY"
tags:
- ingratitude
- humanity
- character
- judgment
- truth
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Apr-2012)
CREATE (t:THOUGHT {
    name: "thought.UNGRATEFUL HUMAN RACE",
    alias: "Thought: Ungrateful Human Race",
    parent: "topic.HUMANITY",
    tags: ['ingratitude', 'humanity', 'character', 'judgment', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNGRATEFUL HUMAN RACE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNGRATEFUL HUMAN RACE" AND c.name = "content.UNGRATEFUL HUMAN RACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNGRATEFUL HUMAN RACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.UNGRATEFUL HUMAN RACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >UNGRATEFUL HUMAN RACE" }]->(child);
```
