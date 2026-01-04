---
name: "thought.ELECTROMAGNETISM TOUCH"
alias: "Thought: Electromagnetism Touch"
type: THOUGHT
parent: "topic.CREATION"
tags:
- science
- physics
- creation
- design
- power
level: 2
neo4j: true
insert: true
---
# Electromagnetism Touch

> [!Thought-en]
> Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.ELECTROMAGNETISM TOUCH",
    alias: "Thought: Electromagnetism Touch",
    parent: "topic.CREATION",
    tags: ['science', 'physics', 'creation', 'design', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ELECTROMAGNETISM TOUCH",
    en_title: "Electromagnetism Touch",
    en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!",
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
WHERE t.name = "thought.ELECTROMAGNETISM TOUCH" AND c.name = "content.ELECTROMAGNETISM TOUCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ELECTROMAGNETISM TOUCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.ELECTROMAGNETISM TOUCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >ELECTROMAGNETISM TOUCH" }]->(child);
```