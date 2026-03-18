---
type: THOUGHT
name: "thought.COOKED FOOD HUMANS"
alias: "Thought: Cooked Food Humans"
parent:
en_content: "Why are humans the only creatures on planet earth that eat cooked food?"
tags: ["creation", "humanity", "nature", "food", "mystery"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-May-2012a)
CREATE (t:THOUGHT {    name: "thought.COOKED FOOD HUMANS",
    alias: "Thought: Cooked Food Humans",
    parent: "topic.CREATION",
    tags: ['creation', 'humanity', 'nature', 'food', 'mystery'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.COOKED FOOD HUMANS",
    ctype: "THOUGHT",
    en_title: "Cooked Food Humans",
    en_content: "Why are humans the only creatures on planet earth that eat cooked food?",
    es_title: "Comida Cocida Humanos",
    es_content: "¿Por qué los humanos son las únicas criaturas en el planeta tierra que comen comida cocida?",
    fr_title: "Nourriture Cuite Humains",
    fr_content: "Pourquoi les humains sont-ils les seules créatures sur la planète Terre à manger de la nourriture cuite ?",
    hi_title: "पकाया हुआ भोजन मनुष्य",
    hi_content: "मनुष्य पृथ्वी ग्रह पर पकाया हुआ भोजन खाने वाले एकमात्र जीव क्यों हैं?",
    zh_title: "Pēng Rèn Shíwù de Rénlèi",
    zh_content: "Wèishéme rénlèi shì dìqiú shàng wéiyī chī pēng rèn shíwù de shēngwù?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.COOKED FOOD HUMANS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.CREATION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.CREATION->COOKED FOOD HUMANS"
RETURN t, parent;
```
