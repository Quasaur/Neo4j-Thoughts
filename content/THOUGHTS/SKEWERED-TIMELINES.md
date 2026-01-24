---
name: "thought.SKEWERED_TIMELINES"
alias: "Thought: SKEWERED TIMELINES"
type: THOUGHT
parent: topic.HISTORY
tags:
- evolution
- pseudoscience
- timelines
- religion
- creation
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SKEWERED_TIMELINES",
    alias: "Thought: SKEWERED TIMELINES",
    parent: "topic.HISTORY",
    tags: ["evolution", "pseudoscience", "timelines", "religion", "creation"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SKEWERED_TIMELINES",
    en_title: "SKEWERED TIMELINES",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SKEWERED_TIMELINES" AND c.name = "content.SKEWERED_TIMELINES"
MERGE (t)-[:HAS_CONTENT {name: "edge.SKEWERED_TIMELINES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.SKEWERED_TIMELINES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->SKEWERED_TIMELINES"}]->(child);
```
