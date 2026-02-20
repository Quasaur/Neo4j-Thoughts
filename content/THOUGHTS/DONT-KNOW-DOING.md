---
name: thought.DONT KNOW DOING
alias: "Thought: We're Lost!"
type: THOUGHT
en_content: "God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34"
parent: topic.MERCY
tags:
  - forgiveness
  - ignorance
  - humanity
  - mercy
  - bible
level: 5
neo4j: true
ptopic: "[[topic-MERCY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.DONT KNOW DOING",
    alias: "Thought: We're Lost!",
    parent: "topic.MERCY",
    tags: ['forgiveness', 'ignorance', 'humanity', 'mercy', 'bible'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.DONT KNOW DOING",
    en_title: "We're Lost!",
    en_content: "God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34",
    es_title: "Nosotras estamos perdidas",
    es_content: "¡Dios! ¡Perdónanos! ¡¡NO SABEMOS LO QUE HACEMOS!! Lucas 23:34",
    fr_title: "Nous sommes perdus !",
    fr_content: "Dieu! Pardonne-nous! NOUS NE SAVONS PAS CE QUE NOUS FAISONS!! Luc 23:34",
    hi_title: "हम खो गए हैं!",
    hi_content: "हे परमेश्वर! हमें क्षमा करें! हम नहीं जानते कि हम क्या कर रहे हैं!! लूका 23:34",
    zh_title: "Wǒmen mílùle!",
    zh_content: "Shen a! Kuan shu wo men! WO MEN BU ZHI DAO ZI JI ZAI ZUO SHEN ME!! Lu jia fu yin 23:34"
});

MATCH (t:THOUGHT {name: "thought.DONT KNOW DOING"})
MATCH (c:CONTENT {name: "content.DONT KNOW DOING"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.DONT KNOW DOING" }]->(c);

MATCH (parent:TOPIC {name: "topic.MERCY"})
MATCH (child:THOUGHT {name: "thought.DONT KNOW DOING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.MERCY->DONT KNOW DOING" }]->(child);
```
