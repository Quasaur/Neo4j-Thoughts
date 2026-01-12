---
name: "thought.THE FIRST SIN"
alias: "Thought: The First Sin"
type: THOUGHT
en_content: "The First Sinner committed the First Sin by taking the credit for that which he did not create: himself."
parent: "topic.HUMANITY"
tags:
- sin
- pride
- creation
- identity
- humanity
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.THE FIRST SIN",
    alias: "Thought: The First Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'pride', 'creation', 'identity', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE FIRST SIN",
    en_title: "The First Sin",
    en_content: "The First Sinner committed the First Sin by taking the credit for that which he did not create: himself.",
    es_title: "El Primer Pecado",
    es_content: "El Primer Pecador cometió el Primer Pecado al atribuirse el mérito de aquello que no creó: a sí mismo.",
    fr_title: "Le Premier Péché",
    fr_content: "Le Premier Pécheur a commis le Premier Péché en s'attribuant le mérite de ce qu'il n'a pas créé : lui-même.",
    hi_title: "प्रथम पाप",
    hi_content: "प्रथम पापी ने प्रथम पाप किया था उस चीज़ का श्रेय लेकर जिसे उसने बनाया नहीं था: स्वयं को।",
    zh_title: "Dì Yī Zuì",
    zh_content: "Dì Yī Gè Zuìrén fànxià le Dì Yī Zuì, tā bǎ tā méiyǒu chuàngzào de dōngxi guīgōng yú zìjǐ: tā zìjǐ."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE FIRST SIN" AND c.name = "content.THE FIRST SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.THE FIRST SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.THE FIRST SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >THE FIRST SIN" }]->(child);
```
