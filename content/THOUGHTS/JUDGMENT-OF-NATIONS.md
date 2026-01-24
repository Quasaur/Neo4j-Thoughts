---
name: "thought.JUDGMENT OF NATIONS"
alias: "Thought: Judgment Of Nations"
type: THOUGHT
en_content: "God will not only judge individuals, but nations (ethnic and political). May God grant repentance to the USA."
parent: "topic.APOCALYPSE"
tags:
- judgment
- nations
- politics
- repentance
- sovereignty
level: 5
neo4j: true
ptopic: "[[topic-APOCALYPSE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2011b)
CREATE (t:THOUGHT {
    name: "thought.JUDGMENT OF NATIONS",
    alias: "Thought: Judgment Of Nations",
    parent: "topic.APOCALYPSE",
    tags: ['judgment', 'nations', 'politics', 'repentance', 'sovereignty'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.JUDGMENT OF NATIONS",
    en_title: "Judgment Of Nations",
    en_content: "God will not only judge individuals, but nations (ethnic and political). May God grant repentance to the USA.",
    es_title: "Juicio de las Naciones",
    es_content: "Dios no solo juzgará a los individuos, sino a las naciones (étnicas y políticas). Que Dios conceda arrepentimiento a los Estados Unidos.",
    fr_title: "Jugement des Nations",
    fr_content: "Dieu ne jugera pas seulement les individus, mais les nations (ethniques et politiques). Que Dieu accorde la repentance aux États-Unis.",
    hi_title: "राष्ट्रों का न्याय",
    hi_content: "परमेश्वर न केवल व्यक्तियों का न्याय करेगा, बल्कि राष्ट्रों का भी (जातीय और राजनीतिक)। परमेश्वर संयुक्त राज्य अमेरिका को पश्चाताप प्रदान करे।",
    zh_title: "Wàn Guó Shěn Pàn",
    zh_content: "Shàng Dì bù jǐn yào shěn pàn gè rén, ér qiě yào shěn pàn wàn guó (zú qún hé zhèng zhì). Yuàn Shàng Dì cì gěi Měi Guó huǐ gǎi."
});

MATCH (t:THOUGHT {name: "thought.JUDGMENT OF NATIONS"})
MATCH (c:CONTENT {name: "content.JUDGMENT OF NATIONS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.JUDGMENT OF NATIONS" }]->(c);

MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MATCH (child:THOUGHT {name: "thought.JUDGMENT OF NATIONS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "APOCALYPSE->JUDGMENT OF NATIONS" }]->(child);
```
