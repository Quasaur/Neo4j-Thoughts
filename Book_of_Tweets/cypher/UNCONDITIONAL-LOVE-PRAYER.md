---
name: "thought.UNCONDITIONAL LOVE PRAYER"
alias: "Thought: Unconditional Love Prayer"
type: THOUGHT
en_content: "Prayer is where I am loved unconditionally."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- love
- acceptance
- spirituality
- presence
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013f)
CREATE (t:THOUGHT {
    name: "thought.UNCONDITIONAL LOVE PRAYER",
    alias: "Thought: Unconditional Love Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'love', 'acceptance', 'spirituality', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL LOVE PRAYER",
    en_title: "Unconditional Love Prayer",
    en_content: "Prayer is where I am loved unconditionally.",
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
WHERE t.name = "thought.UNCONDITIONAL LOVE PRAYER" AND c.name = "content.UNCONDITIONAL LOVE PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNCONDITIONAL LOVE PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.UNCONDITIONAL LOVE PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >UNCONDITIONAL LOVE PRAYER" }]->(child);
```
