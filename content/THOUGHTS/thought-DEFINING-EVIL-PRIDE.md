---
type: THOUGHT
name: "thought.DEFINING EVIL PRIDE"
alias: "Thought: Defining Evil Pride"
parent: "topic.EVIL"
en_content: "Evil is considering this God-given treasure (Self) more precious than The God Who gave it."
tags: ["evil", "pride", "self", "treasure", "character"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINING EVIL PRIDE",
    alias: "Thought: Defining Evil Pride",
    parent: "topic.EVIL",
    tags: ['evil', 'pride', 'self', 'treasure', 'character'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINING EVIL PRIDE",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINING EVIL PRIDE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DEFINING EVIL PRIDE"
RETURN t, parent;
```
