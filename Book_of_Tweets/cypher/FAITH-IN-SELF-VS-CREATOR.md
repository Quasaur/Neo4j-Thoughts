---
name: "thought.FAITH IN SELF VS CREATOR"
alias: "Thought: Faith In Self Vs Creator"
type: THOUGHT
en_content: "We have more faith in ourselves than we have in our Creator; this is a recipe for disaster."
parent: "topic.FAITH"
tags:
- faith
- self
- creator
- disaster
- trust
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Sep-2011d)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN SELF VS CREATOR",
    alias: "Thought: Faith In Self Vs Creator",
    parent: "topic.FAITH",
    tags: ['faith', 'self', 'creator', 'disaster', 'trust'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN SELF VS CREATOR",
    en_title: "Faith In Self Vs Creator",
    en_content: "We have more faith in ourselves than we have in our Creator; this is a recipe for disaster.",
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
WHERE t.name = "thought.FAITH IN SELF VS CREATOR" AND c.name = "content.FAITH IN SELF VS CREATOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH IN SELF VS CREATOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH IN SELF VS CREATOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >FAITH IN SELF VS CREATOR" }]->(child);
```
