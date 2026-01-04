---
name: "thought.BETTER NOT EASIER"
alias: "Thought: Better Not Easier"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- jesus
- better
- easier
- life
level: 1
neo4j: true
insert: true
---
# Better Not Easier

> [!Thought-en]
> Jesus did not come to make our lives easier; Christ came to make our lives better!

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.BETTER NOT EASIER",
    alias: "Thought: Better Not Easier",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'better', 'easier', 'life'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.BETTER NOT EASIER",
    en_title: "Better Not Easier",
    en_content: "Jesus did not come to make our lives easier; Christ came to make our lives better!",
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
WHERE t.name = "thought.BETTER NOT EASIER" AND c.name = "content.BETTER NOT EASIER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BETTER NOT EASIER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.BETTER NOT EASIER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >BETTER NOT EASIER" }]->(child);
```