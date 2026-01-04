---
name: "thought.SCIENCE AND SCRIPTURE"
alias: "Thought: Science And Scripture"
type: THOUGHT
en_content: "No discrepancy exists between Science and Scripture; the discrepancy is between scientists and God."
parent: "topic.TRUTH"
tags:
- science
- scripture
- truth
- creation
- reconciliation
level: 2
neo4j: true
insert: true
---
# Science And Scripture

> [!Thought-en]
> No discrepancy exists between Science and Scripture; the discrepancy is between scientists and God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.SCIENCE AND SCRIPTURE",
    alias: "Thought: Science And Scripture",
    parent: "topic.TRUTH",
    tags: ['science', 'scripture', 'truth', 'creation', 'reconciliation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SCIENCE AND SCRIPTURE",
    en_title: "Science And Scripture",
    en_content: "No discrepancy exists between Science and Scripture; the discrepancy is between scientists and God.",
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
WHERE t.name = "thought.SCIENCE AND SCRIPTURE" AND c.name = "content.SCIENCE AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SCIENCE AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SCIENCE AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SCIENCE AND SCRIPTURE" }]->(child);
```