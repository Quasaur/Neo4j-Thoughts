---
name: "thought.HEARING AND OBEYING"
alias: "Thought: Hearing And Obeying"
type: THOUGHT
en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it."
parent: "topic.SPIRITUALITY"
tags:
- obedience
- guidance
- spirituality
- listening
- faith
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.HEARING AND OBEYING",
    alias: "Thought: Hearing And Obeying",
    parent: "topic.SPIRITUALITY",
    tags: ['obedience', 'guidance', 'spirituality', 'listening', 'faith'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEARING AND OBEYING",
    en_title: "Hearing And Obeying",
    en_content: "Half the battle: Hearing God's Voice; the Other Half: obeying it.",
    es_title: "Escuchar y obedecer",
    es_content: "La mitad de la batalla: escuchar la voz de Dios;la Otra Mitad: obedecerla.",
    fr_title: "Entendre et obéir",
    fr_content: "La moitié de la bataille : entendre la voix de Dieu ;l'autre moitié : lui obéir.",
    hi_title: "सुनना और पालन करना",
    hi_content: "आधी लड़ाई: भगवान की आवाज सुनना;दूसरा भाग: इसका पालन करना।",
    zh_title: "聆听与服从",
    zh_content: "成功一半：聆听上帝的声音；另一半：服从它。"
});

MATCH (t:THOUGHT {name: "thought.HEARING AND OBEYING"})
MATCH (c:CONTENT {name: "content.HEARING AND OBEYING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEARING AND OBEYING" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.HEARING AND OBEYING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HEARING AND OBEYING" }]->(child);
```
