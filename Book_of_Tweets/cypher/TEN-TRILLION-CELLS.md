---
name: "thought.TEN TRILLION CELLS"
alias: "Thought: Ten Trillion Cells"
type: THOUGHT
en_content: "The human body is made up of at least 10 trillion cells...God is great!"
parent: "topic.CREATION"
tags:
- creation
- biology
- cells
- life
- power
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.TEN TRILLION CELLS",
    alias: "Thought: Ten Trillion Cells",
    parent: "topic.CREATION",
    tags: ['creation', 'biology', 'cells', 'life', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TEN TRILLION CELLS",
    en_title: "Ten Trillion Cells",
    en_content: "The human body is made up of at least 10 trillion cells...God is great!",
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
WHERE t.name = "thought.TEN TRILLION CELLS" AND c.name = "content.TEN TRILLION CELLS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TEN TRILLION CELLS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.TEN TRILLION CELLS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >TEN TRILLION CELLS" }]->(child);
```
