---
name: "thought.WEIGHT OF GREED"
alias: "Thought: Weight Of Greed"
type: THOUGHT
en_content: "America is finally buckling under the weight of its own greed."
parent: "topic.MORALITY"
tags:
- greed
- society
- america
- economics
- judgment
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.WEIGHT OF GREED",
    alias: "Thought: Weight Of Greed",
    parent: "topic.MORALITY",
    tags: ['greed', 'society', 'america', 'economics', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WEIGHT OF GREED",
    en_title: "Weight Of Greed",
    en_content: "America is finally buckling under the weight of its own greed.",
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
WHERE t.name = "thought.WEIGHT OF GREED" AND c.name = "content.WEIGHT OF GREED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WEIGHT OF GREED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.WEIGHT OF GREED"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >WEIGHT OF GREED" }]->(child);
```
