---
name: "thought.MYSTERY OF WOMAN"
alias: "Thought: Mystery Of Woman"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- woman
- man
- mystery
- creation
- adam
level: 3
neo4j: true
insert: true
---
# Mystery Of Woman

> [!Thought-en]
> Adam did not see Eve being created; therefore Woman will always be a Mystery to Man.

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2012)
CREATE (t:THOUGHT {
    name: "thought.MYSTERY OF WOMAN",
    alias: "Thought: Mystery Of Woman",
    parent: "topic.HUMANITY",
    tags: ['woman', 'man', 'mystery', 'creation', 'adam'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MYSTERY OF WOMAN",
    en_title: "Mystery Of Woman",
    en_content: "Adam did not see Eve being created; therefore Woman will always be a Mystery to Man.",
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
WHERE t.name = "thought.MYSTERY OF WOMAN" AND c.name = "content.MYSTERY OF WOMAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MYSTERY OF WOMAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.MYSTERY OF WOMAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >MYSTERY OF WOMAN" }]->(child);
```