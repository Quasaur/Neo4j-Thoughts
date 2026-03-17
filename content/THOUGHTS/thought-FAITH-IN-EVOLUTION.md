---
type: THOUGHT
name: "thought.FAITH IN EVOLUTION"
alias: "Thought: Faith In Evolution"
parent: "topic.PHILOSOPHY"
en_content: "Evolution requires FAR MORE FAITH than Intelligent Design."
tags: ["faith", "evolution", "design", "creation", "science"]
ptopic: "[[topic-PHILOSOPHY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FAITH IN EVOLUTION",
    alias: "Thought: Faith In Evolution",
    parent: "topic.PHILOSOPHY",
    tags: ['faith', 'evolution', 'design', 'creation', 'science'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH IN EVOLUTION",
    ctype: "THOUGHT",
    en_title: "Faith In Evolution",
    en_content: "Evolution requires FAR MORE FAITH than Intelligent Design.",
    es_title: "Fe en la evolución",
    es_content: "La evolución requiere MUCHA MÁS FE que el Diseño Inteligente.",
    fr_title: "Foi en l'évolution",
    fr_content: "L’évolution nécessite BEAUCOUP PLUS DE FOI que la conception intelligente.",
    hi_title: "विकास में विश्वास",
    hi_content: "विकास के लिए बुद्धिमान डिज़ाइन की तुलना में कहीं अधिक विश्वास की आवश्यकता होती है।",
    zh_title: "xiāng xìn jìn huà lùn",
    zh_content: "jìn huà bǐ zhì néng shè jì xū yào gèng duō de xìn niàn 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAITH IN EVOLUTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->FAITH IN EVOLUTION"
RETURN t, parent;
```
