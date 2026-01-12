---
name: "thought.LOSING MY MIND"
alias: "Thought: Losing My Mind"
type: THOUGHT
en_content: "I was insane until I lost my mind!"
parent: "topic.PSYCHOLOGY"
tags:
- insanity
- mind
- psychology
- paradox
- clarity
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LOSING MY MIND",
    alias: "Thought: Losing My Mind",
    parent: "topic.PSYCHOLOGY",
    tags: ['insanity', 'mind', 'psychology', 'paradox', 'clarity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOSING MY MIND",
    en_title: "Losing My Mind",
    en_content: "I was insane until I lost my mind!",
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
WHERE t.name = "thought.LOSING MY MIND" AND c.name = "content.LOSING MY MIND"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOSING MY MIND" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LOSING MY MIND"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >LOSING MY MIND" }]->(child);
```
