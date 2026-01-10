---
name: "thought.FORGIVING THE FUTURE"
alias: "Thought: Forgiving The Future"
type: THOUGHT
en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future."
parent: "topic.GRACE"
tags:
- forgiveness
- future
- past
- grace
- healing
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING THE FUTURE",
    alias: "Thought: Forgiving The Future",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'future', 'past', 'grace', 'healing'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING THE FUTURE",
    en_title: "Forgiving The Future",
    en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future.",
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
WHERE t.name = "thought.FORGIVING THE FUTURE" AND c.name = "content.FORGIVING THE FUTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FORGIVING THE FUTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FORGIVING THE FUTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >FORGIVING THE FUTURE" }]->(child);
```
