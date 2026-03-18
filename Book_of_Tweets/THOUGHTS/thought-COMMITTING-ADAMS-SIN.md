---
type: THOUGHT
name: "thought.COMMITTING ADAMS SIN"
alias: "Thought: Committing Adams Sin"
parent: "topic.HUMANITY"
en_content: "We continue to commit Adam's sin, and then wonder why we suffer."
tags: ["sin", "adam", "suffering", "humanity", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2013a)
CREATE (t:THOUGHT {    name: "thought.COMMITTING ADAMS SIN",
    alias: "Thought: Committing Adams Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'adam', 'suffering', 'humanity', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.COMMITTING ADAMS SIN",
    ctype: "THOUGHT",
    en_title: "Committing Adams Sin",
    en_content: "We continue to commit Adam's sin, and then wonder why we suffer.",
    es_title: "Cometiendo el Pecado de Adán",
    es_content: "Continuamos cometiendo el pecado de Adán, y luego nos preguntamos por qué sufrimos.",
    fr_title: "Commettre le Péché d'Adam",
    fr_content: "Nous continuons à commettre le péché d'Adam, puis nous nous demandons pourquoi nous souffrons.",
    hi_title: "आदम के पाप को करना",
    hi_content: "हम आदम के पाप को करते रहते हैं, और फिर हैरान होते हैं कि हम क्यों पीड़ित हैं।",
    zh_title: "Fàn Ādāng de Zuì",
    zh_content: "Wǒmen jìxù fàn Ādāng de zuì, Ránhòu yòu qíguài wèishénme wǒmen shòukǔ."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COMMITTING ADAMS SIN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->COMMITTING ADAMS SIN"
RETURN t, parent;
```
