---
name: "thought.DONT KNOW DOING"
alias: "Thought: Dont Know Doing"
type: THOUGHT
en_content: "God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34"
parent: "topic.GRACE"
tags:
- forgiveness
- ignorance
- humanity
- grace
- bible
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.DONT KNOW DOING",
    alias: "Thought: Dont Know Doing",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'ignorance', 'humanity', 'grace', 'bible'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DONT KNOW DOING",
    en_title: "Dont Know Doing",
    en_content: "God! Forgive us! WE DON'T KNOW WHAT WE'RE DOING!! Luke 23:34",
    es_title: "No Sabemos Lo Que Hacemos",
    es_content: "¡Dios! ¡Perdónanos! ¡¡NO SABEMOS LO QUE HACEMOS!! Lucas 23:34",
    fr_title: "Ne Savent Pas Ce Qu'ils Font",
    fr_content: "Dieu! Pardonne-nous! NOUS NE SAVONS PAS CE QUE NOUS FAISONS!! Luc 23:34",
    hi_title: "नहीं जानते क्या कर रहे",
    hi_content: "हे परमेश्वर! हमें क्षमा करें! हम नहीं जानते कि हम क्या कर रहे हैं!! लूका 23:34",
    zh_title: "Bu Zhi Dao Zai Zuo Shen Me",
    zh_content: "Shen a! Kuan shu wo men! WO MEN BU ZHI DAO ZI JI ZAI ZUO SHEN ME!! Lu jia fu yin 23:34"
});

MATCH (t:THOUGHT {name: "thought.DONT KNOW DOING"})
MATCH (c:CONTENT {name: "content.DONT KNOW DOING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DONT KNOW DOING" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.DONT KNOW DOING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE->DONT KNOW DOING" }]->(child);
```
