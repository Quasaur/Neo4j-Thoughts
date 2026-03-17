---
type: THOUGHT
name: "thought.LIMITS OF FORGIVENESS"
alias: "Thought: Limits Of Forgiveness"
parent: "topic.GRACE"
en_content: "The only people God doesn't forgive are those who don't want to be forgiven."
tags: ["forgiveness", "grace", "repentance", "will", "mercy"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LIMITS OF FORGIVENESS",
    alias: "Thought: Limits Of Forgiveness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'repentance', 'will', 'mercy'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIMITS OF FORGIVENESS",
    ctype: "THOUGHT",
    en_title: "Limits Of Forgiveness",
    en_content: "The only people God doesn't forgive are those who don't want to be forgiven.",
    es_title: "Límites del perdón",
    es_content: "Las únicas personas que Dios no perdona son aquellas que no quieren ser perdonadas.",
    fr_title: "Limites du pardon",
    fr_content: "Les seules personnes que Dieu ne pardonne pas sont celles qui ne veulent pas être pardonnées.",
    hi_title: "क्षमा की सीमा",
    hi_content: "केवल उन्हीं लोगों को ईश्वर क्षमा नहीं करता है जो क्षमा नहीं चाहते हैं।",
    zh_title: "kuān shù de xiàn dù",
    zh_content: "shén wéi yī bù ráo shù de rén shì nà xiē bù xiǎng bèi ráo shù de rén 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LIMITS OF FORGIVENESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LIMITS OF FORGIVENESS"
RETURN t, parent;
```
