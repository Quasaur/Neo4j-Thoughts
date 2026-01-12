---
name: "thought.FEAR AND SELFISHNESS"
alias: "Thought: Fear And Selfishness"
type: THOUGHT
en_content: "Fear wouldn't be so debilitating if I were not so selfish."
parent: "topic.PSYCHOLOGY"
tags:
- fear
- selfishness
- psychology
- emotion
- character
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.FEAR AND SELFISHNESS",
    alias: "Thought: Fear And Selfishness",
    parent: "topic.PSYCHOLOGY",
    tags: ['fear', 'selfishness', 'psychology', 'emotion', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FEAR AND SELFISHNESS",
    en_title: "Fear And Selfishness",
    en_content: "Fear wouldn't be so debilitating if I were not so selfish.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FEAR AND SELFISHNESS" AND c.name = "content.FEAR AND SELFISHNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FEAR AND SELFISHNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.FEAR AND SELFISHNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >FEAR AND SELFISHNESS" }]->(child);
```
