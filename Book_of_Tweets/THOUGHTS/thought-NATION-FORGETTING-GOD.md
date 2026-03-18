---
type: THOUGHT
name: "thought.NATION FORGETTING GOD"
alias: "Thought: Nation Forgetting God"
parent: "topic.MORALITY"
en_content: "I'm watching a nation that has forgotten God turn into Hell."
tags: ["nation", "hell", "god", "morality", "judgment"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2013a)
CREATE (t:THOUGHT {    name: "thought.NATION FORGETTING GOD",
    alias: "Thought: Nation Forgetting God",
    parent: "topic.MORALITY",
    tags: ['nation', 'hell', 'god', 'morality', 'judgment'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.NATION FORGETTING GOD",
    ctype: "THOUGHT",
    en_title: "Nation Forgetting God",
    en_content: "I'm watching a nation that has forgotten God turn into Hell.",
    es_title: "Nación Olvidando a Dios",
    es_content: "Estoy viendo a una nación que ha olvidado a Dios convertirse en el Infierno.",
    fr_title: "Nation Oubliant Dieu",
    fr_content: "Je regarde une nation qui a oublié Dieu se transformer en Enfer.",
    hi_title: "राष्ट्र परमेश्वर को भूलना",
    hi_content: "मैं एक ऐसे राष्ट्र को देख रहा हूँ जो परमेश्वर को भूल गया है और नरक में बदल रहा है।",
    zh_title: "Guójiā Wàngjì Shàngdì",
    zh_content: "Wǒ zhèngzài kànzhe yī gè wàngjì le Shàngdì de guójiā biànchéng dìyù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NATION FORGETTING GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->NATION FORGETTING GOD"
RETURN t, parent;
```
