---
type: THOUGHT
name: "thought.IN HIM WE LIVE"
alias: "Thought: In Him We Live"
parent: "topic.CREATION"
en_content: "We are all inside of God...is God inside of us?"
tags: ["creation", "divine", "fulness", "indwelling", "holy_spirit"]
ptopic: "[[topic-CREATION]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.IN HIM WE LIVE",
    alias: "Thought: In Him We Live",
    parent: "topic.CREATION",
    tags: ["creation", "divine", "fulness", "indwelling", "holy_spirit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IN HIM WE LIVE",
    ctype: "THOUGHT",
    en_title: "In Him We Live",
    en_content: "We are all inside of God...is God inside of us?",
    es_title: "EN ÉL VIVIMOS",
    es_content: "Todos estamos dentro de Dios... ¿está Dios dentro de nosotros?",
    fr_title: "EN LUI NOUS VIVONS",
    fr_content: "Nous sommes tous à l’intérieur de Dieu… Dieu est-il à l’intérieur de nous ?",
    hi_title: "हम उसी में रहते हैं",
    hi_content: "हम सब भगवान के अंदर हैं...क्या भगवान हमारे अंदर हैं?",
    zh_title: "wǒ men zhù zài tā lǐ miàn",
    zh_content: "wǒ men dōu zài shàng dì zhī nèi …… shàng dì zài wǒ men zhī nèi ma ？"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IN HIM WE LIVE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->IN HIM WE LIVE"
RETURN t, parent;
```
