---
name: "thought.UNIVERSAL MERCY REQUIREMENT"
alias: "Thought: Universal Mercy Requirement"
type: THOUGHT
en_content: "God has to have mercy on everybody in order to save anybody."
parent: "topic.GRACE"
tags:
- mercy
- grace
- salvation
- humanity
- god
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.UNIVERSAL MERCY REQUIREMENT",
    alias: "Thought: Universal Mercy Requirement",
    parent: "topic.GRACE",
    tags: ['mercy', 'grace', 'salvation', 'humanity', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNIVERSAL MERCY REQUIREMENT",
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

MATCH (t:THOUGHT {name: "thought.UNIVERSAL MERCY REQUIREMENT"})
MATCH (c:CONTENT {name: "content.UNIVERSAL MERCY REQUIREMENT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNIVERSAL MERCY REQUIREMENT" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.UNIVERSAL MERCY REQUIREMENT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->UNIVERSAL MERCY REQUIREMENT" }]->(child);
```
