---
name: "thought.HUMAN BREATHS DAILY"
alias: "Thought: Human Breaths Daily"
type: THOUGHT
en_content: "The average human takes 17,280-23,040 breaths per day; God is great!"
parent: "topic.CREATION"
tags:
- creation
- biology
- life
- breath
- power
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.HUMAN BREATHS DAILY",
    alias: "Thought: Human Breaths Daily",
    parent: "topic.CREATION",
    tags: ['creation', 'biology', 'life', 'breath', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HUMAN BREATHS DAILY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN BREATHS DAILY" AND c.name = "content.HUMAN BREATHS DAILY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMAN BREATHS DAILY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HUMAN BREATHS DAILY"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >HUMAN BREATHS DAILY" }]->(child);
```
