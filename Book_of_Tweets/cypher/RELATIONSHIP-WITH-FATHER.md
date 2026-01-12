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
ptopic: 
---

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
    es_title: "Relación con el Padre",
    es_content: "El Evangelio: ¡Jesucristo nos ha dado Su Relación con el Padre!",
    fr_title: "Relation avec le Père",
    fr_content: "L'Évangile : Jésus-Christ nous a donné Sa Relation avec le Père !",
    hi_title: "पिता के साथ रिश्ता",
    hi_content: "सुसमाचार: यीशु मसीह ने हमें पिता के साथ अपना रिश्ता दिया है!",
    zh_title: "Yu Tianfu De Guanxi",
    zh_content: "Fuyin: Yesu Jidu yi jiang Ta yu Tianfu de guanxi ci gei le women!"
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
