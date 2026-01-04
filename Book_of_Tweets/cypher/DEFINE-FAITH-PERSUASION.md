---
name: "thought.DEFINE FAITH PERSUASION"
alias: "Thought: Define Faith Persuasion"
type: THOUGHT
en_content: "Faith is not me persuading God to keep His Promises, but God persuading me that He is watching over His Word to perform It."
parent: "topic.FAITH"
tags:
- faith
- persuasion
- promises
- god
- truth
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013c)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH PERSUASION",
    alias: "Thought: Define Faith Persuasion",
    parent: "topic.FAITH",
    tags: ['faith', 'persuasion', 'promises', 'god', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH PERSUASION",
    en_title: "Define Faith Persuasion",
    en_content: "Faith is not me persuading God to keep His Promises, but God persuading me that He is watching over His Word to perform It.",
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
WHERE t.name = "thought.DEFINE FAITH PERSUASION" AND c.name = "content.DEFINE FAITH PERSUASION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE FAITH PERSUASION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DEFINE FAITH PERSUASION"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE FAITH PERSUASION" }]->(child);
```
