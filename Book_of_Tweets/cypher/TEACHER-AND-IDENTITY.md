---
name: "thought.TEACHER AND IDENTITY"
alias: "Thought: Teacher And Identity"
type: THOUGHT
en_content: "A teacher challenges your identity and your knowledge, then helps you discover both so that you can stand strong under pressure."
parent: "topic.WISDOM"
tags:
- wisdom
- teaching
- identity
- growth
- knowledge
level: 3
neo4j: true
insert: true
---
# Teacher And Identity

> [!Thought-en]
> A teacher challenges your identity and your knowledge, then helps you discover both so that you can stand strong under pressure.

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.TEACHER AND IDENTITY",
    alias: "Thought: Teacher And Identity",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'teaching', 'identity', 'growth', 'knowledge'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TEACHER AND IDENTITY",
    en_title: "Teacher And Identity",
    en_content: "A teacher challenges your identity and your knowledge, then helps you discover both so that you can stand strong under pressure.",
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
WHERE t.name = "thought.TEACHER AND IDENTITY" AND c.name = "content.TEACHER AND IDENTITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TEACHER AND IDENTITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.TEACHER AND IDENTITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >TEACHER AND IDENTITY" }]->(child);
```