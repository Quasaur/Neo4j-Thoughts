---
type: THOUGHT
name: "thought.GLOVES"
alias: "Thought: Gloves"
parent: "topic.EVANGELISM"
tags: ["vessel", "instrument", "gospel", "missionaries", "believers"]
ptopic: "[[topic-EVANGELISM]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GLOVES",
    alias: "Thought: Gloves",
    parent: "topic.EVANGELISM",
    tags: ["vessel", "instrument", "gospel", "missionaries", "believers"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLOVES",
    ctype: "THOUGHT",
    en_title: "Gloves",
    en_content: "God is not looking for hands...He's looking for gloves!",
    es_title: "GUANTES",
    es_content: "Dios no busca manos... ¡Busca guantes!",
    fr_title: "GANTS",
    fr_content: "Dieu ne cherche pas des mains... Il cherche des gants !",
    hi_title: "दस्ताने",
    hi_content: "भगवान हाथों की तलाश में नहीं है...वह दस्ताने की तलाश में है!",
    zh_title: "shǒu tào",
    zh_content: "shàng dì bú shì zài xún zhǎo shuāng shǒu …… tā shì zài xún zhǎo shǒu tào ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GLOVES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVANGELISM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVANGELISM->GLOVES"
RETURN t, parent;
```
