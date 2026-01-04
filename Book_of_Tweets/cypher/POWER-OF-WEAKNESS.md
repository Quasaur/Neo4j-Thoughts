---
name: "thought.POWER OF WEAKNESS"
alias: "Thought: Power Of Weakness"
type: THOUGHT
en_content: "True Strength understands the Power of Weakness."
parent: "topic.WISDOM"
tags:
- strength
- weakness
- power
- wisdom
- character
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012a)
CREATE (t:THOUGHT {
    name: "thought.POWER OF WEAKNESS",
    alias: "Thought: Power Of Weakness",
    parent: "topic.WISDOM",
    tags: ['strength', 'weakness', 'power', 'wisdom', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.POWER OF WEAKNESS",
    en_title: "Power Of Weakness",
    en_content: "True Strength understands the Power of Weakness.",
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
WHERE t.name = "thought.POWER OF WEAKNESS" AND c.name = "content.POWER OF WEAKNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.POWER OF WEAKNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.POWER OF WEAKNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >POWER OF WEAKNESS" }]->(child);
```
