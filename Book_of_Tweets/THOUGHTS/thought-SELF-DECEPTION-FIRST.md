---
type: THOUGHT
name: "thought.SELF DECEPTION FIRST"
alias: "Thought: Self Deception First"
parent: "topic.PSYCHOLOGY"
en_content: "To deceive another, you must first deceive yourself."
tags: ["deception", "self", "psychology", "honesty", "character"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2012)
CREATE (t:THOUGHT {    name: "thought.SELF DECEPTION FIRST",
    alias: "Thought: Self Deception First",
    parent: "topic.PSYCHOLOGY",
    tags: ['deception', 'self', 'psychology', 'honesty', 'character'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.SELF DECEPTION FIRST",
    ctype: "THOUGHT",
    en_title: "Self Deception First",
    en_content: "To deceive another, you must first deceive yourself.",
    es_title: "Primero el Autoengaño",
    es_content: "Para engañar a otro, primero debes engañarte a ti mismo.",
    fr_title: "L'Auto-Tromperie d'Abord",
    fr_content: "Pour tromper autrui, il faut d'abord se tromper soi-même.",
    hi_title: "पहले आत्म-प्रवंचना",
    hi_content: "दूसरे को धोखा देने के लिए, पहले आपको अपने आप को धोखा देना होगा।",
    zh_title: "Zi Qi Qian Xian",
    zh_content: "Yao qi pian ta ren, ni bi xu xian qi pian zi ji."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SELF DECEPTION FIRST"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->SELF DECEPTION FIRST"
RETURN t, parent;
```
