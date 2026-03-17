---
type: THOUGHT
name: "thought.WEEPING OVER CREATION"
alias: "Thought: Ecological Care"
parent: "topic.ENVIRONMENTAL SCIENCE"
en_content: "(Weeping over BP Oil Spill)."
tags: ["creation", "sorrow", "environment", "stewardship", "pollution"]
ptopic: "[[topic-ENVIRONMENTAL-SCIENCE]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WEEPING OVER CREATION",
    alias: "Thought: Ecological Care",
    parent: "topic.ENVIRONMENTAL SCIENCE",
    tags: ["creation", "sorrow", "environment", "stewardship", "pollution"],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.WEEPING OVER CREATION",
    ctype: "THOUGHT",
    en_title: "Weeping over Creation",
    en_content: "(Weeping over BP Oil Spill).",
    es_title: "Llorando por creación",
    es_content: "(Llorando por el derrame de petróleo de BP).",
    fr_title: "Pleurs sur la création",
    fr_content: "(Pleurant sur la marée noire de BP).",
    hi_title: "srshti par rona",
    hi_content: "(बीपी तेल रिसाव पर रोते हुए)।",
    zh_title: "Wèi chuàngzào kūqì",
    zh_content: "( wèi BP shí yóu xiè lòu kū qì )."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WEEPING OVER CREATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->WEEPING OVER CREATION"
RETURN t, parent;
```
