---
name: "thought.COOKED FOOD HUMANS"
alias: "Thought: Cooked Food Humans"
type: THOUGHT
en_content: "Why are humans the only creatures on planet earth that eat cooked food?"
parent: "topic.CREATION"
tags:
- creation
- humanity
- nature
- food
- mystery
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-May-2012a)
CREATE (t:THOUGHT {
    name: "thought.COOKED FOOD HUMANS",
    alias: "Thought: Cooked Food Humans",
    parent: "topic.CREATION",
    tags: ['creation', 'humanity', 'nature', 'food', 'mystery'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COOKED FOOD HUMANS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.COOKED FOOD HUMANS" AND c.name = "content.COOKED FOOD HUMANS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COOKED FOOD HUMANS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.COOKED FOOD HUMANS"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >COOKED FOOD HUMANS" }]->(child);
```
