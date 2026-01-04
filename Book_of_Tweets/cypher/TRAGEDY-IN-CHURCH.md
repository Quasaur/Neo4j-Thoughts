---
name: "thought.TRAGEDY IN CHURCH"
alias: "Thought: Tragedy In Church"
type: THOUGHT
parent: "topic.RELIGION"
tags:
- religion
- church
- salvation
- tragedy
- deception
level: 3
neo4j: true
insert: true
---
# Tragedy In Church

> [!Thought-en]
> To be in church all one's life, and still go to Hell...what a tragedy!

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.TRAGEDY IN CHURCH",
    alias: "Thought: Tragedy In Church",
    parent: "topic.RELIGION",
    tags: ['religion', 'church', 'salvation', 'tragedy', 'deception'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TRAGEDY IN CHURCH",
    en_title: "Tragedy In Church",
    en_content: "To be in church all one's life, and still go to Hell...what a tragedy!",
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
WHERE t.name = "thought.TRAGEDY IN CHURCH" AND c.name = "content.TRAGEDY IN CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRAGEDY IN CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.TRAGEDY IN CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >TRAGEDY IN CHURCH" }]->(child);
```