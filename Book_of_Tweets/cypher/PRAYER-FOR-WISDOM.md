---
name: "thought.PRAYER FOR WISDOM"
alias: "Thought: Prayer For Wisdom"
type: THOUGHT
en_content: "Lord Jesus, fill my mind with Your Wisdom; fill my heart with Your Love; fill my bowels with Your Mercy!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- wisdom
- love
- mercy
- jesus
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.PRAYER FOR WISDOM",
    alias: "Thought: Prayer For Wisdom",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'wisdom', 'love', 'mercy', 'jesus'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER FOR WISDOM",
    en_title: "Prayer For Wisdom",
    en_content: "Lord Jesus, fill my mind with Your Wisdom; fill my heart with Your Love; fill my bowels with Your Mercy!",
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
WHERE t.name = "thought.PRAYER FOR WISDOM" AND c.name = "content.PRAYER FOR WISDOM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER FOR WISDOM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER FOR WISDOM"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER FOR WISDOM" }]->(child);
```
