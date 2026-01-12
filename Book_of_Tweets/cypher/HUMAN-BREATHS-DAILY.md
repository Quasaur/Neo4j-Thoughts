---
name: "thought.HUMAN BREATHS DAILY"
alias: "Thought: Human Breaths Daily"
type: THOUGHT
en_content: "The average human takes 17,280-23,040 breaths per day; God is great!"
parent: "topic.CREATION"
tags:
- creation
- biology
- life
- breath
- power
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.HUMAN BREATHS DAILY",
    alias: "Thought: Human Breaths Daily",
    parent: "topic.CREATION",
    tags: ['creation', 'biology', 'life', 'breath', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HUMAN BREATHS DAILY",
    en_title: "Human Breaths Daily",
    en_content: "The average human takes 17,280-23,040 breaths per day; God is great!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN BREATHS DAILY" AND c.name = "content.HUMAN BREATHS DAILY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMAN BREATHS DAILY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HUMAN BREATHS DAILY"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >HUMAN BREATHS DAILY" }]->(child);
```
