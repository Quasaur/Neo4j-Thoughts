---
name: "thought.CHEMICAL VIRTUE"
alias: "Thought: Chemical Virtue"
type: THOUGHT
en_content: "You yourself are a supernatural being! Explain LOVE, or COURAGE or VIRTUE chemically."
parent: "topic.PHILOSOPHY"
tags:
- supernatural
- love
- courage
- chemistry
- philosophy
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011f)
CREATE (t:THOUGHT {
    name: "thought.CHEMICAL VIRTUE",
    alias: "Thought: Chemical Virtue",
    parent: "topic.PHILOSOPHY",
    tags: ['supernatural', 'love', 'courage', 'chemistry', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHEMICAL VIRTUE",
    en_title: "Chemical Virtue",
    en_content: "You yourself are a supernatural being! Explain LOVE, or COURAGE or VIRTUE chemically.",
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
WHERE t.name = "thought.CHEMICAL VIRTUE" AND c.name = "content.CHEMICAL VIRTUE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHEMICAL VIRTUE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.CHEMICAL VIRTUE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >CHEMICAL VIRTUE" }]->(child);
```
