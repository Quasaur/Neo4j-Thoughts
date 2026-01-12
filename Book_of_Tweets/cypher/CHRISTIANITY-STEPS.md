---
name: "thought.CHRISTIANITY STEPS"
alias: "Thought: Christianity Steps"
type: THOUGHT
en_content: "Christianity: READ, HEAR, BELIEVE, CONFESS, OBEY, ASK, RECEIVE."
parent: "topic.RELIGION"
tags:
- faith
- steps
- christianity
- obedience
- belief
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.CHRISTIANITY STEPS",
    alias: "Thought: Christianity Steps",
    parent: "topic.RELIGION",
    tags: ['faith', 'steps', 'christianity', 'obedience', 'belief'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHRISTIANITY STEPS",
    en_title: "Christianity Steps",
    en_content: "Christianity: READ, HEAR, BELIEVE, CONFESS, OBEY, ASK, RECEIVE.",
    es_title: "Pasos del Cristianismo",
    es_content: "Cristianismo: LEER, OÍR, CREER, CONFESAR, OBEDECER, PEDIR, RECIBIR.",
    fr_title: "Étapes du Christianisme",
    fr_content: "Christianisme : LIRE, ENTENDRE, CROIRE, CONFESSER, OBÉIR, DEMANDER, RECEVOIR.",
    hi_title: "ईसाई धर्म के कदम",
    hi_content: "ईसाई धर्म: पढ़ें, सुनें, विश्वास करें, कबूल करें, आज्ञा मानें, मांगें, प्राप्त करें।",
    zh_title: "Jīdūjiào de Bùzhòu",
    zh_content: "Jīdūjiào: YÈDÚ, TĪNG, XIĀNGXÌN, CHÉNGRÈN, SHÙNCHÓNG, QÐQIÚ, JIĒSHÒU."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHRISTIANITY STEPS" AND c.name = "content.CHRISTIANITY STEPS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTIANITY STEPS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHRISTIANITY STEPS"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHRISTIANITY STEPS" }]->(child);
```
