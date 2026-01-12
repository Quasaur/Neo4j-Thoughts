---
name: "thought.SEEKING VS HEARING GOD"
alias: "Thought: Seeking Vs Hearing God"
type: THOUGHT
en_content: "You would think that a person desperate to hear from God would be desperate to seek God..."
parent: "topic.SPIRITUALITY"
tags:
- seeking
- hearing
- god
- desperation
- spirituality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.SEEKING VS HEARING GOD",
    alias: "Thought: Seeking Vs Hearing God",
    parent: "topic.SPIRITUALITY",
    tags: ['seeking', 'hearing', 'god', 'desperation', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SEEKING VS HEARING GOD",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SEEKING VS HEARING GOD" AND c.name = "content.SEEKING VS HEARING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SEEKING VS HEARING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SEEKING VS HEARING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SEEKING VS HEARING GOD" }]->(child);
```
