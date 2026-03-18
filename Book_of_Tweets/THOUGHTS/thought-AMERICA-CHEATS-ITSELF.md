---
type: THOUGHT
name: "thought.AMERICA CHEATS ITSELF"
alias: "Thought: America Cheats Itself"
parent: "topic.MORALITY"
en_content: "America is a nation that CHEATS ITSELF out of its own money."
tags: ["america", "economy", "greed", "morality", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2011)
CREATE (t:THOUGHT {    name: "thought.AMERICA CHEATS ITSELF",
    alias: "Thought: America Cheats Itself",
    parent: "topic.MORALITY",
    tags: ['america', 'economy', 'greed', 'morality', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.AMERICA CHEATS ITSELF",
    ctype: "THOUGHT",
    en_title: "America Cheats Itself",
    en_content: "America is a nation that CHEATS ITSELF out of its own money.",
    es_title: "América se Engaña a Sí Misma",
    es_content: "América es una nación que SE ENGAÑA A SÍ MISMA quitándose su propio dinero.",
    fr_title: "L'Amérique se Trompe Elle-même",
    fr_content: "L'Amérique est une nation qui SE TROMPE ELLE-MÊME en se privant de son propre argent.",
    hi_title: "अमेरिका स्वयं को धोखा देता है",
    hi_content: "अमेरिका एक ऐसा राष्ट्र है जो अपने ही पैसे से खुद को धोखा देता है।",
    zh_title: "Měiguó qīpiàn zìjǐ",
    zh_content: "Měiguó shì yīgè qīpiàn zìjǐ, bōduó zìjǐ jīnqián de guójiā."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.AMERICA CHEATS ITSELF"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->AMERICA CHEATS ITSELF"
RETURN t, parent;
```
