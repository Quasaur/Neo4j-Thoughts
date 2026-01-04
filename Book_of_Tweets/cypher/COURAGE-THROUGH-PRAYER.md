---
name: "thought.COURAGE THROUGH PRAYER"
alias: "Thought: Courage Through Prayer"
type: THOUGHT
en_content: "Prayer is where I find Courage and Perseverance."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- courage
- perseverance
- spirituality
- strength
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013g)
CREATE (t:THOUGHT {
    name: "thought.COURAGE THROUGH PRAYER",
    alias: "Thought: Courage Through Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'courage', 'perseverance', 'spirituality', 'strength'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COURAGE THROUGH PRAYER",
    en_title: "Courage Through Prayer",
    en_content: "Prayer is where I find Courage and Perseverance.",
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
WHERE t.name = "thought.COURAGE THROUGH PRAYER" AND c.name = "content.COURAGE THROUGH PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COURAGE THROUGH PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.COURAGE THROUGH PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >COURAGE THROUGH PRAYER" }]->(child);
```
