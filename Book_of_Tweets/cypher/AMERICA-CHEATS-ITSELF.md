---
name: "thought.AMERICA CHEATS ITSELF"
alias: "Thought: America Cheats Itself"
type: THOUGHT
en_content: "America is a nation that CHEATS ITSELF out of its own money."
parent: "topic.MORALITY"
tags:
- america
- economy
- greed
- morality
- society
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.AMERICA CHEATS ITSELF",
    alias: "Thought: America Cheats Itself",
    parent: "topic.MORALITY",
    tags: ['america', 'economy', 'greed', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AMERICA CHEATS ITSELF",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMERICA CHEATS ITSELF" AND c.name = "content.AMERICA CHEATS ITSELF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AMERICA CHEATS ITSELF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AMERICA CHEATS ITSELF"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AMERICA CHEATS ITSELF" }]->(child);
```
