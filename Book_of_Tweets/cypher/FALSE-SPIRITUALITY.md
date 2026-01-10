---
name: "thought.FALSE SPIRITUALITY"
alias: "Thought: False Spirituality"
type: THOUGHT
en_content: "False Spirituality: placing the Devil around every corner, under every rock and behind every bush to cover defects of character."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- deception
- devil
- character
- excuse
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.FALSE SPIRITUALITY",
    alias: "Thought: False Spirituality",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'deception', 'devil', 'character', 'excuse'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FALSE SPIRITUALITY",
    en_title: "False Spirituality",
    en_content: "False Spirituality: placing the Devil around every corner, under every rock and behind every bush to cover defects of character.",
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
WHERE t.name = "thought.FALSE SPIRITUALITY" AND c.name = "content.FALSE SPIRITUALITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FALSE SPIRITUALITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FALSE SPIRITUALITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FALSE SPIRITUALITY" }]->(child);
```
