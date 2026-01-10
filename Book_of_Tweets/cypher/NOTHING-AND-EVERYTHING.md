---
name: "thought.NOTHING AND EVERYTHING"
alias: "Thought: Nothing And Everything"
type: THOUGHT
en_content: "I am nothing to God...and yet...I am everything to God."
parent: "topic.HUMANITY"
tags:
- humanity
- god
- value
- identity
- paradox
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.NOTHING AND EVERYTHING",
    alias: "Thought: Nothing And Everything",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'god', 'value', 'identity', 'paradox'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOTHING AND EVERYTHING",
    en_title: "Nothing And Everything",
    en_content: "I am nothing to God...and yet...I am everything to God.",
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
WHERE t.name = "thought.NOTHING AND EVERYTHING" AND c.name = "content.NOTHING AND EVERYTHING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING AND EVERYTHING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.NOTHING AND EVERYTHING"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >NOTHING AND EVERYTHING" }]->(child);
```
