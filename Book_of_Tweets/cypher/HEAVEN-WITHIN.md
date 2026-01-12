---
name: "thought.HEAVEN WITHIN"
alias: "Thought: Heaven Within"
type: THOUGHT
en_content: "If Heaven isn't in us, then we can't go to Heaven."
parent: "topic.SPIRITUALITY"
tags:
- heaven
- spirituality
- eternity
- transformation
- presence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2010b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN WITHIN",
    alias: "Thought: Heaven Within",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'spirituality', 'eternity', 'transformation', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN",
    en_title: "Heaven Within",
    en_content: "If Heaven isn't in us, then we can't go to Heaven.",
    es_title: "El cielo interior",
    es_content: "Si el Cielo no está en nosotros, entonces no podemos ir al Cielo.",
    fr_title: "Le paradis intérieur",
    fr_content: "Si le Ciel n’est pas en nous, alors nous ne pouvons pas aller au Ciel.",
    hi_title: "भीतर स्वर्ग",
    hi_content: "यदि स्वर्ग हमारे अंदर नहीं है तो हम स्वर्ग में नहीं जा सकते।",
    zh_title: "天堂之内",
    zh_content: "如果天堂不在我们里面，那么我们就不能去天堂。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEAVEN WITHIN" AND c.name = "content.HEAVEN WITHIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN WITHIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HEAVEN WITHIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEAVEN WITHIN" }]->(child);
```
