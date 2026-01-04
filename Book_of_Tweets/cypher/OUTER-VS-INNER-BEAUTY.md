---
name: "thought.OUTER VS INNER BEAUTY"
alias: "Thought: Outer Vs Inner Beauty"
type: THOUGHT
en_content: "Outer beauty doesn't make up for inner ugly."
parent: "topic.BEAUTY"
tags:
- beauty
- character
- appearance
- aesthetics
- holiness
level: 6
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.OUTER VS INNER BEAUTY",
    alias: "Thought: Outer Vs Inner Beauty",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'character', 'appearance', 'aesthetics', 'holiness'],
    notes: "",
    level: 6
});

CREATE (c:CONTENT {
    name: "content.OUTER VS INNER BEAUTY",
    en_title: "Outer Vs Inner Beauty",
    en_content: "Outer beauty doesn't make up for inner ugly.",
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
WHERE t.name = "thought.OUTER VS INNER BEAUTY" AND c.name = "content.OUTER VS INNER BEAUTY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OUTER VS INNER BEAUTY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.OUTER VS INNER BEAUTY"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >OUTER VS INNER BEAUTY" }]->(child);
```
