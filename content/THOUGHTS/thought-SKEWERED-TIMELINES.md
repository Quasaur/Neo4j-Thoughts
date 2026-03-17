---
type: THOUGHT
name: "thought.SKEWERED TIMELINES"
alias: "Thought: Skewered Timelines"
parent: "topic.HISTORY"
en_content: "To prove evolution, so-called science has completely skewered the chronological, geological and human timelines."
tags: ["evolution", "pseudoscience", "timelines", "religion", "creation"]
ptopic: "[[topic-HISTORY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SKEWERED TIMELINES",
    alias: "Thought: Skewered Timelines",
    parent: "topic.HISTORY",
    tags: ["evolution", "pseudoscience", "timelines", "religion", "creation"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SKEWERED TIMELINES",
    ctype: "THOUGHT",
    en_title: "Skewered Timelines",
    en_content: "To prove evolution, so-called science has completely skewered the chronological, geological and human timelines.",
    es_title: "CRONOGRAMAS ENCHUFADOS",
    es_content: "Para demostrar la evolución, la llamada ciencia ha trastocado por completo las líneas de tiempo cronológicas, geológicas y humanas.",
    fr_title: "DES CHRONOLOGIES BROCHÉES",
    fr_content: "Pour prouver l’évolution, la soi-disant science a complètement brouillé les chronologies chronologiques, géologiques et humaines.",
    hi_title: "तिरछी समयरेखाएँ",
    hi_content: "विकास को सिद्ध करने के लिए, तथाकथित विज्ञान ने कालानुक्रमिक, भूवैज्ञानिक और मानव समयरेखा को पूरी तरह से विकृत कर दिया है।",
    zh_title: "chuàn shāo de shí jiān biǎo",
    zh_content: "wèi le zhèng míng jìn huà lùn ， suǒ wèi de kē xué wán quán wāi qū le nián dài 、 dì zhì hé rén lèi de shí jiān xiàn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SKEWERED TIMELINES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HISTORY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HISTORY->SKEWERED TIMELINES"
RETURN t, parent;
```
