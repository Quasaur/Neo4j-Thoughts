---
name: "thought.SUFFERING VS SINNING"
alias: "Thought: Suffering Vs Sinning"
type: THOUGHT
en_content: "We are tired of suffering, yet we are not tired of sinning."
parent: "topic.HUMANITY"
tags:
- suffering
- sin
- humanity
- paradox
- attitude
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011d)
CREATE (t:THOUGHT {
    name: "thought.SUFFERING VS SINNING",
    alias: "Thought: Suffering Vs Sinning",
    parent: "topic.HUMANITY",
    tags: ['suffering', 'sin', 'humanity', 'paradox', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SUFFERING VS SINNING",
    en_title: "Suffering Vs Sinning",
    en_content: "We are tired of suffering, yet we are not tired of sinning.",
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
WHERE t.name = "thought.SUFFERING VS SINNING" AND c.name = "content.SUFFERING VS SINNING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SUFFERING VS SINNING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.SUFFERING VS SINNING"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >SUFFERING VS SINNING" }]->(child);
```
