---
name: "thought.GRACE VS MERIT"
alias: "Thought: Grace Vs Merit"
type: THOUGHT
en_content: "The merit system and Grace are incompatible...we have to choose one or the other."
parent: "topic.GRACE"
tags:
- grace
- merit
- salvation
- choice
- gospel
level: 3
neo4j: true
ptopic: "[[topic-GRACE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS MERIT",
    alias: "Thought: Grace Vs Merit",
    parent: "topic.GRACE",
    tags: ['grace', 'merit', 'salvation', 'choice', 'gospel'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE VS MERIT",
    en_title: "Grace Vs Merit",
    en_content: "The merit system and Grace are incompatible...we have to choose one or the other.",
    es_title: "Gracia versus Mérito",
    es_content: "El sistema de méritos y la Gracia son incompatibles... tenemos que elegir uno u otro.",
    fr_title: "Grâce contre Mérite",
    fr_content: "Le système de mérite et la Grâce sont incompatibles... nous devons choisir l'un ou l'autre.",
    hi_title: "कृपा बनाम योग्यता",
    hi_content: "योग्यता प्रणाली और कृपा असंगत हैं... हमें एक या दूसरा चुनना होगा।",
    zh_title: "Ēndiǎn yǔ gōngjixué  ēn diǎn yǔ gōng jì shuō",
    zh_content: "Gōngjixué zhìduù hé ēndiǎn shì bù xiāng róng de... wǒmen bìxū xuǎnzé qí yī.  gōng jì shuō zhì dù hé ēn diǎn shì bù xiāng róng de ... wǒ men bì xū xuǎn zé qí yī 。"
});

MATCH (t:THOUGHT {name: "thought.GRACE VS MERIT"})
MATCH (c:CONTENT {name: "content.GRACE VS MERIT"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.GRACE VS MERIT" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.GRACE VS MERIT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.GRACE->GRACE VS MERIT" }]->(child);
```
