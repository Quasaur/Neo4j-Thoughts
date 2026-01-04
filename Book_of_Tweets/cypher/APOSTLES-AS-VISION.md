---
name: "thought.APOSTLES AS VISION"
alias: "Thought: Apostles As Vision"
type: THOUGHT
parent: "topic.RELIGION"
tags:
- apostles
- vision
- jesus
- church
- history
level: 3
neo4j: true
insert: true
---
# Apostles As Vision

> [!Thought-en]
> The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.APOSTLES AS VISION",
    alias: "Thought: Apostles As Vision",
    parent: "topic.RELIGION",
    tags: ['apostles', 'vision', 'jesus', 'church', 'history'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.APOSTLES AS VISION",
    en_title: "Apostles As Vision",
    en_content: "The Apostles loved Jesus' Vision because the Apostles WERE Jesus' Vision!",
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
WHERE t.name = "thought.APOSTLES AS VISION" AND c.name = "content.APOSTLES AS VISION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.APOSTLES AS VISION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.APOSTLES AS VISION"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >APOSTLES AS VISION" }]->(child);
```