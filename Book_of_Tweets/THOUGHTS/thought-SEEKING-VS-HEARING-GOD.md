---
type: THOUGHT
name: "thought.SEEKING VS HEARING GOD"
alias: "Thought: Seeking Vs Hearing God"
parent: "topic.SPIRITUALITY"
en_content: "You would think that a person desperate to hear from God would be desperate to seek God..."
tags: ["seeking", "hearing", "god", "desperation", "spirituality"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013b)
CREATE (t:THOUGHT {    name: "thought.SEEKING VS HEARING GOD",
    alias: "Thought: Seeking Vs Hearing God",
    parent: "topic.SPIRITUALITY",
    tags: ['seeking', 'hearing', 'god', 'desperation', 'spirituality'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.SEEKING VS HEARING GOD",
    ctype: "THOUGHT",
    en_title: "Seeking Vs Hearing God",
    en_content: "You would think that a person desperate to hear from God would be desperate to seek God...",
    es_title: "Buscar Vs Escuchar a Dios",
    es_content: "Uno pensaría que una persona desesperada por escuchar de Dios estaría desesperada por buscar a Dios...",
    fr_title: "Chercher Vs Entendre Dieu",
    fr_content: "On pourrait penser qu'une personne désespérée d'entendre Dieu serait désespérée de chercher Dieu...",
    hi_title: "परमेश्वर को खोजना बनाम परमेश्वर को सुनना",
    hi_content: "आप सोचेंगे कि जो व्यक्ति परमेश्वर से सुनने के लिए बेताब है, वह परमेश्वर को खोजने के लिए भी बेताब होगा...",
    zh_title: "Xun Qiu Vs Ting Jian Shen",
    zh_content: "Ni hui ren wei yi ge po qie xi wang ting dao Shen sheng yin de ren ye hui po qie de xun qiu Shen..."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SEEKING VS HEARING GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.SPIRITUALITY->SEEKING VS HEARING GOD"
RETURN t, parent;
```
