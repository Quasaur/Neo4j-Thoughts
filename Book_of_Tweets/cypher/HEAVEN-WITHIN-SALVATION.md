---
name: "thought.HEAVEN WITHIN SALVATION"
alias: "Thought: Heaven Within Salvation"
type: THOUGHT
en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you."
parent: "topic.GRACE"
tags:
- salvation
- heaven
- transformation
- grace
- presence
level: 3
neo4j: true
insert: true
---
# Heaven Within Salvation

> [!Thought-en]
> The objective of Salvation is not to get you into Heaven, but to get Heaven into you.

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN WITHIN SALVATION",
    alias: "Thought: Heaven Within Salvation",
    parent: "topic.GRACE",
    tags: ['salvation', 'heaven', 'transformation', 'grace', 'presence'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN SALVATION",
    en_title: "Heaven Within Salvation",
    en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you.",
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
WHERE t.name = "thought.HEAVEN WITHIN SALVATION" AND c.name = "content.HEAVEN WITHIN SALVATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN WITHIN SALVATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.HEAVEN WITHIN SALVATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >HEAVEN WITHIN SALVATION" }]->(child);
```