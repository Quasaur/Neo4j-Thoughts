---
type: THOUGHT
name: "thought.OPPORTUNITY FOR ANGER"
alias: "Thought: Opportunity For Anger"
parent: "topic.ATTITUDE"
en_content: "People don't need a reason to be angry...just an opportunity."
tags: ["anger", "attitude", "character", "human_nature", "emotion"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.OPPORTUNITY FOR ANGER",
    alias: "Thought: Opportunity For Anger",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'attitude', 'character', 'human_nature', 'emotion'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OPPORTUNITY FOR ANGER",
    ctype: "THOUGHT",
    en_title: "Opportunity For Anger",
    en_content: "People don't need a reason to be angry...just an opportunity.",
    es_title: "Oportunidad Para La Ira",
    es_content: "Las personas no necesitan una razón para estar enojadas...solo una oportunidad.",
    fr_title: "Opportunité Pour La Colère",
    fr_content: "Les gens n'ont pas besoin d'une raison pour être en colère...juste d'une opportunité.",
    hi_title: "क्रोध के लिए अवसर",
    hi_content: "लोगों को गुस्सा होने के लिए किसी कारण की जरूरत नहीं...बस एक अवसर की।",
    zh_title: "Fen Nu De Ji Hui",
    zh_content: "Ren men bu xu yao sheng qi de li you...zhi xu yao yi ge ji hui."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.OPPORTUNITY FOR ANGER"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->OPPORTUNITY FOR ANGER"
RETURN t, parent;
```
