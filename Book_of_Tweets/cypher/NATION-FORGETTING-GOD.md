---
name: "thought.NATION FORGETTING GOD"
alias: "Thought: Nation Forgetting God"
type: THOUGHT
en_content: "I'm watching a nation that has forgotten God turn into Hell."
parent: "topic.MORALITY"
tags:
- nation
- hell
- god
- morality
- judgment
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.NATION FORGETTING GOD",
    alias: "Thought: Nation Forgetting God",
    parent: "topic.MORALITY",
    tags: ['nation', 'hell', 'god', 'morality', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NATION FORGETTING GOD",
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

MATCH (t:THOUGHT {name: "thought.NATION FORGETTING GOD"})
MATCH (c:CONTENT {name: "content.NATION FORGETTING GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATION FORGETTING GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.NATION FORGETTING GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >NATION FORGETTING GOD" }]->(child);
```
