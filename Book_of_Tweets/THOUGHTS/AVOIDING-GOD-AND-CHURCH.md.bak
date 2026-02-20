---
name: "thought.AVOIDING GOD AND CHURCH"
alias: "Thought: Avoiding God And Church"
type: THOUGHT
en_content: "Why do African American men avoid God and His Church???"
parent: "topic.RELIGION"
tags:
- church
- religion
- race
- avoid
- faith
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012b)
CREATE (t:THOUGHT {
    name: "thought.AVOIDING GOD AND CHURCH",
    alias: "Thought: Avoiding God And Church",
    parent: "topic.RELIGION",
    tags: ['church', 'religion', 'race', 'avoid', 'faith'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.AVOIDING GOD AND CHURCH",
    en_title: "Avoiding God And Church",
    en_content: "Why do African American men avoid God and His Church???",
    es_title: "Evitando a Dios y la Iglesia",
    es_content: "¿Por qué los hombres afroamericanos evitan a Dios y Su Iglesia???",
    fr_title: "Éviter Dieu et l'Église",
    fr_content: "Pourquoi les hommes afro-américains évitent-ils Dieu et Son Église ???",
    hi_title: "परमेश्वर और चर्च से बचना",
    hi_content: "अफ्रीकी अमेरिकी पुरुष परमेश्वर और उनके चर्च से क्यों बचते हैं???",
    zh_title: "Bìmiǎn Shàngdì hé jiàohuì 避免上帝和教会",
    zh_content: "Wèishénme Fēizhōu Měiguó nánxìng yào bìmiǎn Shàngdì hé tā de jiàohuì??? 为什么非洲美国男性要避免上帝和他的教会???"
});

MATCH (t:THOUGHT {name: "thought.AVOIDING GOD AND CHURCH"})
MATCH (c:CONTENT {name: "content.AVOIDING GOD AND CHURCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.AVOIDING GOD AND CHURCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.AVOIDING GOD AND CHURCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->AVOIDING GOD AND CHURCH" }]->(child);
```
