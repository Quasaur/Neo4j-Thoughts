---
name: "thought.PRIDE VS DIGNITY RACE"
alias: "Thought: Pride Vs Dignity Race"
type: THOUGHT
en_content: "Why do African American men confuse pride with dignity?"
parent: "topic.HUMANITY"
tags:
- pride
- dignity
- race
- character
- confusion
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012c)
CREATE (t:THOUGHT {
    name: "thought.PRIDE VS DIGNITY RACE",
    alias: "Thought: Pride Vs Dignity Race",
    parent: "topic.HUMANITY",
    tags: ['pride', 'dignity', 'race', 'character', 'confusion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRIDE VS DIGNITY RACE",
    en_title: "Pride Vs Dignity Race",
    en_content: "Why do African American men confuse pride with dignity?",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIDE VS DIGNITY RACE" AND c.name = "content.PRIDE VS DIGNITY RACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIDE VS DIGNITY RACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.PRIDE VS DIGNITY RACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >PRIDE VS DIGNITY RACE" }]->(child);
```
