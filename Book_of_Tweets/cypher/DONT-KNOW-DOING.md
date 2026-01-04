---
name: "thought.DONT KNOW DOING"
alias: "Thought: Dont Know Doing"
type: THOUGHT
parent: "topic.GRACE"
tags:
- forgiveness
- ignorance
- humanity
- grace
- bible
level: 3
neo4j: true
insert: true
---
# Dont Know Doing

> [!Thought-en]
> God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.DONT KNOW DOING",
    alias: "Thought: Dont Know Doing",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'ignorance', 'humanity', 'grace', 'bible'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DONT KNOW DOING",
    en_title: "Dont Know Doing",
    en_content: "God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34",
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
WHERE t.name = "thought.DONT KNOW DOING" AND c.name = "content.DONT KNOW DOING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DONT KNOW DOING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DONT KNOW DOING"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DONT KNOW DOING" }]->(child);
```