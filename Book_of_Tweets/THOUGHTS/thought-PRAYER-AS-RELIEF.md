---
type: THOUGHT
name: "thought.PRAYER AS RELIEF"
alias: "Thought: Prayer As Relief"
parent: "topic.SPIRITUALITY"
en_content: "Prayer is my relief."
tags: ["prayer", "relief", "pain", "spirituality", "comfort"]
ptopic:
level: 2
neo4j: false
---





```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.PRAYER AS RELIEF",
    alias: "Thought: Prayer As Relief",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'relief', 'pain', 'spirituality', 'comfort'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER AS RELIEF",
    en_title: "Prayer As Relief",
    en_content: "Prayer is my relief.",
    es_title: "La Oración Como Alivio",
    es_content: "La oración es mi alivio.",
    fr_title: "La Prière Comme Soulagement",
    fr_content: "La prière est mon soulagement.",
    hi_title: "राहत के रूप में प्रार्थना",
    hi_content: "प्रार्थना मेरी राहत है।",
    zh_title: "Dǎogào Zuòwéi Ānwèi",
    zh_content: "Dǎogào shì wǒ de ānwèi."
});

MATCH (t:THOUGHT {name: "thought.PRAYER AS RELIEF"})
MATCH (c:CONTENT {name: "content.PRAYER AS RELIEF"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER AS RELIEF" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER AS RELIEF"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRAYER AS RELIEF" }]->(child);
```
