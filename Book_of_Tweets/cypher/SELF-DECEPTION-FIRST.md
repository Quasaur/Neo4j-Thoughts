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
level: 3
neo4j: true
insert: true
---
# Self Deception First

> [!Thought-en]
> To deceive another, you must first deceive yourself.

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.SELF DECEPTION FIRST",
    alias: "Thought: Self Deception First",
    parent: "topic.PSYCHOLOGY",
    tags: ['deception', 'self', 'psychology', 'honesty', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF DECEPTION FIRST",
    en_title: "Self Deception First",
    en_content: "To deceive another, you must first deceive yourself.",
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
WHERE t.name = "thought.SELF DECEPTION FIRST" AND c.name = "content.SELF DECEPTION FIRST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SELF DECEPTION FIRST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.SELF DECEPTION FIRST"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >SELF DECEPTION FIRST" }]->(child);
```