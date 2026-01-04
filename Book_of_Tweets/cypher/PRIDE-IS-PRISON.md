---
name: "thought.PRIDE IS PRISON"
alias: "Thought: Pride Is Prison"
type: THOUGHT
parent: "topic.ATTITUDE"
tags:
- pride
- love
- freedom
- attitude
- liberation
level: 2
neo4j: true
insert: true
---
# Pride Is Prison

> [!Thought-en]
> Pride is a prison, and Unconditional Love the only Liberator.

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.PRIDE IS PRISON",
    alias: "Thought: Pride Is Prison",
    parent: "topic.ATTITUDE",
    tags: ['pride', 'love', 'freedom', 'attitude', 'liberation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRIDE IS PRISON",
    en_title: "Pride Is Prison",
    en_content: "Pride is a prison, and Unconditional Love the only Liberator.",
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
WHERE t.name = "thought.PRIDE IS PRISON" AND c.name = "content.PRIDE IS PRISON"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIDE IS PRISON" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PRIDE IS PRISON"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >PRIDE IS PRISON" }]->(child);
```