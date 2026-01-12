---
name: "thought.NOT DYING ALONE"
alias: "Thought: Not Dying Alone"
type: THOUGHT
en_content: "God will let you die...but He will not let you die alone."
parent: "topic.SPIRITUALITY"
tags:
- death
- comfort
- presence
- spirituality
- compassion
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NOT DYING ALONE",
    alias: "Thought: Not Dying Alone",
    parent: "topic.SPIRITUALITY",
    tags: ['death', 'comfort', 'presence', 'spirituality', 'compassion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOT DYING ALONE",
    en_title: "Not Dying Alone",
    en_content: "God will let you die...but He will not let you die alone.",
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
WHERE t.name = "thought.NOT DYING ALONE" AND c.name = "content.NOT DYING ALONE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT DYING ALONE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NOT DYING ALONE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NOT DYING ALONE" }]->(child);
```
