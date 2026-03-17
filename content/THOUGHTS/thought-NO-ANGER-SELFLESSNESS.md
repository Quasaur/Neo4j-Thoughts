---
type: THOUGHT
name: "thought.NO ANGER SELFLESSNESS"
alias: "Thought: No Anger Selflessness"
parent: "topic.ATTITUDE"
en_content: "There is no anger in selflessness."
tags: ["selflessness", "anger", "attitude", "peace", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NO ANGER SELFLESSNESS",
    alias: "Thought: No Anger Selflessness",
    parent: "topic.ATTITUDE",
    tags: ['selflessness', 'anger', 'attitude', 'peace', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NO ANGER SELFLESSNESS",
    ctype: "THOUGHT",
    en_title: "No Anger Selflessness",
    en_content: "There is no anger in selflessness.",
    es_title: "No Hay Ira en el Desinterés",
    es_content: "No hay ira en el desinterés.",
    fr_title: "Pas de Colère dans le Désintéressement",
    fr_content: "Il n'y a pas de colère dans le désintéressement.",
    hi_title: "निःस्वार्थता में कोई क्रोध नहीं",
    hi_content: "निःस्वार्थता में कोई क्रोध नहीं होता।",
    zh_title: "Wú sī zhōng méiyǒu fènnù 无私中没有愤怒",
    zh_content: "Wú sī zhōng méiyǒu fènnù. 无私中没有愤怒。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NO ANGER SELFLESSNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->NO ANGER SELFLESSNESS"
RETURN t, parent;
```
