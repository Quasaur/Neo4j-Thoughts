---
name: "thought.LIFE FROM INORGANIC"
alias: "Thought: Life From Inorganic"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- life
- biology
- creation
- origin
- god
level: 2
neo4j: true
insert: true
---
# Life From Inorganic

> [!Thought-en]
> In 13 billion years 100 monkeys will never write a novel and life will never rise from inorganic matter without an Act of God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LIFE FROM INORGANIC",
    alias: "Thought: Life From Inorganic",
    parent: "topic.TRUTH",
    tags: ['life', 'biology', 'creation', 'origin', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIFE FROM INORGANIC",
    en_title: "Life From Inorganic",
    en_content: "In 13 billion years 100 monkeys will never write a novel and life will never rise from inorganic matter without an Act of God.",
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
WHERE t.name = "thought.LIFE FROM INORGANIC" AND c.name = "content.LIFE FROM INORGANIC"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIFE FROM INORGANIC" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.LIFE FROM INORGANIC"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >LIFE FROM INORGANIC" }]->(child);
```