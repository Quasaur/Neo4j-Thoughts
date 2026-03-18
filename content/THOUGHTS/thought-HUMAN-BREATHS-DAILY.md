---
type: THOUGHT
name: "thought.HUMAN BREATHS DAILY"
alias: "Thought: Human Breaths Daily"
parent: "topic.BIOLOGY"
en_content: "The average human takes 17,280-23,040 breaths per day; God is great!"
tags: ["creation", "biology", "life", "breath", "power"]
ptopic: "[[topic.BIOLOGY]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMAN BREATHS DAILY",
    alias: "Thought: Human Breaths Daily",
    parent: "topic.BIOLOGY",
    tags: ['creation', 'biology', 'life', 'breath', 'power'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.HUMAN BREATHS DAILY",
    ctype: "THOUGHT",
    en_title: "Human Breaths Daily",
    en_content: "The average human takes 17,280-23,040 breaths per day; God is great!",
    es_title: "Respiraciones Humanas Diarias",
    es_content: "El ser humano promedio toma 17,280-23,040 respiraciones por día; ¡Dios es grande!",
    fr_title: "Respirations Humaines Quotidiennes",
    fr_content: "L'être humain moyen prend 17,280-23,040 respirations par jour ; Dieu est grand !",
    hi_title: "मानव की दैनिक सांसें",
    hi_content: "औसत मानव प्रतिदिन 17,280-23,040 सांसें लेता है; परमेश्वर महान है!",
    zh_title: "Ren Lei Mei Ri De Hu Xi",
    zh_content: "Ping Jun Mei Ge Ren Yi Tian Yao Hu Xi 17,280-23,040 Ci; Shang Di Shi Wei Da De!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMAN BREATHS DAILY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.BIOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.BIOLOGY->HUMAN BREATHS DAILY"
RETURN t, parent;
```
