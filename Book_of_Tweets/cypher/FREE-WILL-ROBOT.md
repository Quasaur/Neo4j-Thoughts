---
name: "thought.FREE WILL ROBOT"
alias: "Thought: Free Will Robot"
type: THOUGHT
en_content: "If you WERE a robot...HOW WOULD YOU KNOW your will wasn't free?"
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- freewill
- consciousness
- robot
- truth
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.FREE WILL ROBOT",
    alias: "Thought: Free Will Robot",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'freewill', 'consciousness', 'robot', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FREE WILL ROBOT",
    en_title: "Free Will Robot",
    en_content: "If you WERE a robot...HOW WOULD YOU KNOW your will wasn't free?",
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
WHERE t.name = "thought.FREE WILL ROBOT" AND c.name = "content.FREE WILL ROBOT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FREE WILL ROBOT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.FREE WILL ROBOT"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >FREE WILL ROBOT" }]->(child);
```
