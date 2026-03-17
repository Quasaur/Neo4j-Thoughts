---
type: THOUGHT
name: "thought.FORGIVING THE FUTURE"
alias: "Thought: Forgiving The Future"
parent: "topic.GRACE"
en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future."
tags: ["forgiveness", "future", "past", "grace", "healing"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING THE FUTURE",
    alias: "Thought: Forgiving The Future",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'future', 'past', 'grace', 'healing'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING THE FUTURE",
    ctype: "THOUGHT",
    en_title: "Forgiving The Future",
    en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future.",
    es_title: "Perdonando el Futuro",
    es_content: "Estamos tan ocupados luchando por perdonar el pasado que nunca consideramos la necesidad de perdonar el futuro.",
    fr_title: "Pardonner l'Avenir",
    fr_content: "Nous sommes si occupés à lutter pour pardonner le passé que nous n'envisageons jamais la nécessité de pardonner l'avenir.",
    hi_title: "भविष्य को क्षमा करना",
    hi_content: "हम अतीत को क्षमा करने के संघर्ष में इतने व्यस्त हैं कि हम भविष्य को क्षमा करने की आवश्यकता पर कभी विचार नहीं करते।",
    zh_title: "Kuanshu Weilai",
    zh_content: "Women mangyu zhengzha kuanshu guoqu, que conglai meiyou kaolü kuanshu weilai de biyaoxing."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FORGIVING THE FUTURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->FORGIVING THE FUTURE"
RETURN t, parent;
```
