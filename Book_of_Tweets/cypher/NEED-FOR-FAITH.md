---
name: "thought.NEED FOR FAITH"
alias: "Thought: Need For Faith"
type: THOUGHT
en_content: "As long as there is ignorance, there will be a need for faith."
parent: "topic.FAITH"
tags:
- faith
- ignorance
- knowledge
- dependence
- philosophy
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NEED FOR FAITH",
    alias: "Thought: Need For Faith",
    parent: "topic.FAITH",
    tags: ['faith', 'ignorance', 'knowledge', 'dependence', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NEED FOR FAITH",
    en_title: "Need For Faith",
    en_content: "As long as there is ignorance, there will be a need for faith.",
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
WHERE t.name = "thought.NEED FOR FAITH" AND c.name = "content.NEED FOR FAITH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NEED FOR FAITH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.NEED FOR FAITH"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >NEED FOR FAITH" }]->(child);
```
