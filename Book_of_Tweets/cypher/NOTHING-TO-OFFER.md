---
name: "thought.NOTHING TO OFFER"
alias: "Thought: Nothing To Offer"
type: THOUGHT
en_content: "God is not interested in what you can offer Him; because the truth is that you have nothing to give God until He gives it to you first!"
parent: "topic.THE GODHEAD"
tags:
- provision
- offering
- dependence
- majesty
- god
level: 1
neo4j: true
insert: true
---
# Nothing To Offer

> [!Thought-en]
> God is not interested in what you can offer Him; because the truth is that you have nothing to give God until He gives it to you first!

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.NOTHING TO OFFER",
    alias: "Thought: Nothing To Offer",
    parent: "topic.THE GODHEAD",
    tags: ['provision', 'offering', 'dependence', 'majesty', 'god'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOTHING TO OFFER",
    en_title: "Nothing To Offer",
    en_content: "God is not interested in what you can offer Him; because the truth is that you have nothing to give God until He gives it to you first!",
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
WHERE t.name = "thought.NOTHING TO OFFER" AND c.name = "content.NOTHING TO OFFER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING TO OFFER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOTHING TO OFFER"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOTHING TO OFFER" }]->(child);
```