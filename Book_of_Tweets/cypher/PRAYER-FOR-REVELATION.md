---
name: "thought.PRAYER FOR REVELATION"
alias: "Thought: Prayer For Revelation"
type: THOUGHT
en_content: "God knows things about the people around you that you have no idea of; if one of those things comes to light, it is so you can pray."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- revelation
- empathy
- spirituality
- discernment
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.PRAYER FOR REVELATION",
    alias: "Thought: Prayer For Revelation",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'revelation', 'empathy', 'spirituality', 'discernment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER FOR REVELATION",
    en_title: "Prayer For Revelation",
    en_content: "God knows things about the people around you that you have no idea of; if one of those things comes to light, it is so you can pray.",
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
WHERE t.name = "thought.PRAYER FOR REVELATION" AND c.name = "content.PRAYER FOR REVELATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER FOR REVELATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER FOR REVELATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER FOR REVELATION" }]->(child);
```
