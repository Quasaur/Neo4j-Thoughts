---
name: "thought.WALKING WITH GOD"
alias: "Thought: Walking With God"
type: THOUGHT
en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit."
parent: "topic.SPIRITUALITY"
tags:
- holyspirit
- enoch
- spirituality
- obedience
- fellowship
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.WALKING WITH GOD",
    alias: "Thought: Walking With God",
    parent: "topic.SPIRITUALITY",
    tags: ['holyspirit', 'enoch', 'spirituality', 'obedience', 'fellowship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WALKING WITH GOD",
    en_title: "Walking With God",
    en_content: "The Bible doesn't say that God walked with Enoch, but that Enoch walked with God. Enoch was led by the Holy Spirit.",
    es_title: "Caminando con Dios",
    es_content: "La Biblia no dice que Dios caminó con Enoc, sino que Enoc caminó con Dios.Enoc fue guiado por el Espíritu Santo.",
    fr_title: "Marcher avec Dieu",
    fr_content: "La Bible ne dit pas que Dieu marchait avec Enoch, mais qu'Enoch marchait avec Dieu.Hénoc était dirigé par le Saint-Esprit.",
    hi_title: "भगवान के साथ चलना",
    hi_content: "बाइबल यह नहीं कहती कि परमेश्वर हनोक के साथ चला, बल्कि यह कि हनोक परमेश्वर के साथ चला।हनोक का नेतृत्व पवित्र आत्मा द्वारा किया गया था।",
    zh_title: "与神同行",
    zh_content: "圣经没有说神与以诺同行，而是说以诺与神同行。以诺是被圣灵引导的。"
});

MATCH (t:THOUGHT {name: "thought.WALKING WITH GOD"})
MATCH (c:CONTENT {name: "content.WALKING WITH GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WALKING WITH GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.WALKING WITH GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->WALKING WITH GOD" }]->(child);
```
