---
name: "thought.DEFINING EVIL PRIDE"
alias: "Thought: Defining Evil Pride"
type: THOUGHT
en_content: "Evil is considering this God-given treasure (Self) more precious than The God Who gave it."
parent: "topic.EVIL"
tags:
- evil
- pride
- self
- treasure
- character
level: 4
neo4j: true
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.DEFINING EVIL PRIDE",
    alias: "Thought: Defining Evil Pride",
    parent: "topic.EVIL",
    tags: ['evil', 'pride', 'self', 'treasure', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINING EVIL PRIDE",
    en_title: "Defining Evil Pride",
    en_content: "Evil is considering this God-given treasure (Self) more precious than The God Who gave it.",
    es_title: "Definiendo el Orgullo Maligno",
    es_content: "El mal es considerar este tesoro dado por Dios (el Ser) más precioso que El Dios Quien lo dio.",
    fr_title: "Définir l'Orgueil Maléfique",
    fr_content: "Le mal, c'est considérer ce trésor donné par Dieu (le Soi) plus précieux que Le Dieu Qui l'a donné.",
    hi_title: "दुष्ट अहंकार की परिभाषा",
    hi_content: "बुराई यह है कि इस ईश्वर-प्रदत्त खजाने (स्व) को उस ईश्वर से अधिक कीमती समझना जिसने इसे दिया है।",
    zh_title: "Ding Yi Xie E De Jiao Ao",
    zh_content: "Xie e jiu shi ba zhe ge Shang Di ci yu de bao zang (Zi Wo) kan de bi ci yu ta de Shang Di geng jia zhen gui."
});

MATCH (t:THOUGHT {name: "thought.DEFINING EVIL PRIDE"})
MATCH (c:CONTENT {name: "content.DEFINING EVIL PRIDE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINING EVIL PRIDE" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.DEFINING EVIL PRIDE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.EVIL->DEFINING EVIL PRIDE" }]->(child);
```
