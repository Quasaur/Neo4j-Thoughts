---
name: "thought.SIN TASTES GOOD"
alias: "Thought: Sin Tastes Good"
type: THOUGHT
en_content: "Sin is killing us; but at least it tastes good!"
parent: "topic.MORALITY"
tags:
- sin
- taste
- irony
- morality
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013b)
CREATE (t:THOUGHT {
    name: "thought.SIN TASTES GOOD",
    alias: "Thought: Sin Tastes Good",
    parent: "topic.MORALITY",
    tags: ['sin', 'taste', 'irony', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN TASTES GOOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SIN TASTES GOOD" AND c.name = "content.SIN TASTES GOOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN TASTES GOOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SIN TASTES GOOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SIN TASTES GOOD" }]->(child);
```
