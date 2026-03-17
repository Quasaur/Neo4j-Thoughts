---
type: THOUGHT
name: "thought.UNIVERSAL MERCY REQUIREMENT"
alias: "Thought: Universal Mercy Requirement"
parent: "topic.MERCY"
en_content: "God has to have mercy on everybody in order to save anybody."
tags: ["mercy", "grace", "salvation", "humanity", "god"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNIVERSAL MERCY REQUIREMENT",
    alias: "Thought: Universal Mercy Requirement",
    parent: "topic.MERCY",
    tags: ['mercy', 'grace', 'salvation', 'humanity', 'god'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.UNIVERSAL MERCY REQUIREMENT",
    ctype: "THOUGHT",
    en_title: "Universal Mercy Requirement",
    en_content: "God has to have mercy on everybody in order to save anybody.",
    es_title: "Requisito de Misericordia Universal",
    es_content: "Dios tiene que tener misericordia de todos para poder salvar a cualquiera.",
    fr_title: "Exigence de Miséricorde Universelle",
    fr_content: "Dieu doit avoir pitié de tout le monde pour pouvoir sauver qui que ce soit.",
    hi_title: "सार्वभौमिक कृपा की आवश्यकता",
    hi_content: "परमेश्वर को किसी को भी बचाने के लिए सभी पर दया करनी होगी।",
    zh_title: "Pǔshì Cíbēi Yāoqiú",
    zh_content: "Shàngdì bìxū duì měi gè rén dōu yǒu cíbēi, cáinéng zhěngjiù rènhé rén."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNIVERSAL MERCY REQUIREMENT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->UNIVERSAL MERCY REQUIREMENT"
RETURN t, parent;
```
