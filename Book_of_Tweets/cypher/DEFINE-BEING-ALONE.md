---
name: "thought.DEFINE BEING ALONE"
alias: "Thought: Define Being Alone"
type: THOUGHT
en_content: "The true definition of being alone is being unaware of God's Loving Presence."
parent: "topic.SPIRITUALITY"
tags:
- alone
- presence
- god
- awareness
- spirituality
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.DEFINE BEING ALONE",
    alias: "Thought: Define Being Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['alone', 'presence', 'god', 'awareness', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEFINE BEING ALONE",
    en_title: "Define Being Alone",
    en_content: "The true definition of being alone is being unaware of God's Loving Presence.",
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
WHERE t.name = "thought.DEFINE BEING ALONE" AND c.name = "content.DEFINE BEING ALONE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE BEING ALONE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.DEFINE BEING ALONE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >DEFINE BEING ALONE" }]->(child);
```
