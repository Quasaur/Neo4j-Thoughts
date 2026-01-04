---
name: "thought.ATOMS IN CELL"
alias: "Thought: Atoms In Cell"
type: THOUGHT
en_content: "The average human cell is made of approx. 200 trillion atoms...God is great!"
parent: "topic.CREATION"
tags:
- creation
- atoms
- biology
- science
- majesty
level: 2
neo4j: true
insert: true
---
# Atoms In Cell

> [!Thought-en]
> The average human cell is made of approx. 200 trillion atoms...God is great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.ATOMS IN CELL",
    alias: "Thought: Atoms In Cell",
    parent: "topic.CREATION",
    tags: ['creation', 'atoms', 'biology', 'science', 'majesty'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ATOMS IN CELL",
    en_title: "Atoms In Cell",
    en_content: "The average human cell is made of approx. 200 trillion atoms...God is great!",
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
WHERE t.name = "thought.ATOMS IN CELL" AND c.name = "content.ATOMS IN CELL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATOMS IN CELL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.ATOMS IN CELL"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >ATOMS IN CELL" }]->(child);
```