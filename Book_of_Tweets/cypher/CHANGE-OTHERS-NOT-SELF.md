---
name: thought.CHANGE OTHERS NOT SELF
alias: "Thought: Change Others Not Self"
type: THOUGHT
en_content: We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.
parent: topic.ATTITUDE
tags:
  - change
  - growth
  - attitude
  - pain
  - transformation
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.CHANGE OTHERS NOT SELF",
    alias: "Thought: Change Others Not Self",
    parent: "topic.ATTITUDE",
    tags: ['change', 'growth', 'attitude', 'pain', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHANGE OTHERS NOT SELF",
    en_title: "Change Others Not Self",
    en_content: "We want God to change everyone but ourselves; for the truth is that change can be a painful process...even when God is performing it.",
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
WHERE t.name = "thought.CHANGE OTHERS NOT SELF" AND c.name = "content.CHANGE OTHERS NOT SELF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGE OTHERS NOT SELF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.CHANGE OTHERS NOT SELF"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >CHANGE OTHERS NOT SELF" }]->(child);
```
