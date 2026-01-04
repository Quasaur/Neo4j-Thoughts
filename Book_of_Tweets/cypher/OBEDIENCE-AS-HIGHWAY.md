---
name: "thought.OBEDIENCE AS HIGHWAY"
alias: "Thought: Obedience As Highway"
type: THOUGHT
en_content: "Obedience is like the lines on a highway: though restrictive, they will take you where you need to go."
parent: "topic.SPIRITUALITY"
tags:
- obedience
- guidance
- restriction
- spirituality
- direction
level: 2
neo4j: true
insert: true
---
# Obedience As Highway

> [!Thought-en]
> Obedience is like the lines on a highway: though restrictive, they will take you where you need to go.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.OBEDIENCE AS HIGHWAY",
    alias: "Thought: Obedience As Highway",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'restriction', 'spirituality', 'direction'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OBEDIENCE AS HIGHWAY",
    en_title: "Obedience As Highway",
    en_content: "Obedience is like the lines on a highway: though restrictive, they will take you where you need to go.",
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
WHERE t.name = "thought.OBEDIENCE AS HIGHWAY" AND c.name = "content.OBEDIENCE AS HIGHWAY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBEDIENCE AS HIGHWAY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.OBEDIENCE AS HIGHWAY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >OBEDIENCE AS HIGHWAY" }]->(child);
```