---
name: "thought.FREEDOM TO RUIN"
alias: "Thought: Freedom To Ruin"
type: THOUGHT
en_content: "It appears that God has given us the freedom to ruin our lives as we see fit...so much for Freedom."
parent: "topic.HUMANITY"
tags:
- freedom
- responsibility
- choice
- humanity
- ruin
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.FREEDOM TO RUIN",
    alias: "Thought: Freedom To Ruin",
    parent: "topic.HUMANITY",
    tags: ['freedom', 'responsibility', 'choice', 'humanity', 'ruin'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FREEDOM TO RUIN",
    en_title: "Freedom To Ruin",
    en_content: "It appears that God has given us the freedom to ruin our lives as we see fit...so much for Freedom.",
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
WHERE t.name = "thought.FREEDOM TO RUIN" AND c.name = "content.FREEDOM TO RUIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FREEDOM TO RUIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.FREEDOM TO RUIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >FREEDOM TO RUIN" }]->(child);
```
