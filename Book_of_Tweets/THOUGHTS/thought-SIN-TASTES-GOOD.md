---
type: THOUGHT
name: "thought.SIN TASTES GOOD"
alias: "Thought: Sin Tastes Good"
parent: "topic.MORALITY"
en_content: "Sin is killing us; but at least it tastes good!"
tags: ["sin", "taste", "irony", "morality", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013b)
CREATE (t:THOUGHT {    name: "thought.SIN TASTES GOOD",
    alias: "Thought: Sin Tastes Good",
    parent: "topic.MORALITY",
    tags: ['sin', 'taste', 'irony', 'morality', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.SIN TASTES GOOD",
    ctype: "THOUGHT",
    en_title: "Sin Tastes Good",
    en_content: "Sin is killing us; but at least it tastes good!",
    es_title: "El Pecado Sabe Bien",
    es_content: "El pecado nos está matando; ¡pero al menos sabe bien!",
    fr_title: "Le Péché a Bon Goût",
    fr_content: "Le péché nous tue ; mais au moins il a bon goût !",
    hi_title: "पाप का स्वाद अच्छा होता है",
    hi_content: "पाप हमें मार रहा है; लेकिन कम से कम इसका स्वाद तो अच्छा है!",
    zh_title: "Zuì'è De Wèidào Hěn Hǎo",
    zh_content: "Zuì'è zhèngzài shāsǐ wǒmen; dàn zhìshǎo tā de wèidào hěn hǎo!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SIN TASTES GOOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->SIN TASTES GOOD"
RETURN t, parent;
```
