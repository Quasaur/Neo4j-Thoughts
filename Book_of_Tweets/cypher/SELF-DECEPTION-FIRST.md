---
name: "thought.SELF DECEPTION FIRST"
alias: "Thought: Self Deception First"
type: THOUGHT
en_content: "To deceive another, you must first deceive yourself."
parent: "topic.PSYCHOLOGY"
tags:
- deception
- self
- psychology
- honesty
- character
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.SELF DECEPTION FIRST",
    alias: "Thought: Self Deception First",
    parent: "topic.PSYCHOLOGY",
    tags: ['deception', 'self', 'psychology', 'honesty', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SELF DECEPTION FIRST",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF DECEPTION FIRST" AND c.name = "content.SELF DECEPTION FIRST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SELF DECEPTION FIRST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.SELF DECEPTION FIRST"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >SELF DECEPTION FIRST" }]->(child);
```
