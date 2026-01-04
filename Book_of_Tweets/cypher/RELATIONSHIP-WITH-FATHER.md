---
name: "thought.RELATIONSHIP WITH FATHER"
alias: "Thought: Relationship With Father"
type: THOUGHT
en_content: "The Gospel: Jesus Christ has given us His Relationship with The Father!"
parent: "topic.THE GODHEAD"
tags:
- father
- relationship
- jesus
- gospel
- gift
level: 1
neo4j: true
insert: true
---
# Relationship With Father

> [!Thought-en]
> The Gospel: Jesus Christ has given us His Relationship with The Father!

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.RELATIONSHIP WITH FATHER",
    alias: "Thought: Relationship With Father",
    parent: "topic.THE GODHEAD",
    tags: ['father', 'relationship', 'jesus', 'gospel', 'gift'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RELATIONSHIP WITH FATHER",
    en_title: "Relationship With Father",
    en_content: "The Gospel: Jesus Christ has given us His Relationship with The Father!",
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
WHERE t.name = "thought.RELATIONSHIP WITH FATHER" AND c.name = "content.RELATIONSHIP WITH FATHER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RELATIONSHIP WITH FATHER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.RELATIONSHIP WITH FATHER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >RELATIONSHIP WITH FATHER" }]->(child);
```