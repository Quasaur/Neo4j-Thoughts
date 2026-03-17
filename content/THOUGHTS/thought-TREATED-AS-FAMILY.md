---
type: THOUGHT
name: "thought.TREATED AS FAMILY"
alias: "Thought: Treated As Family"
parent: "topic.GRACE"
en_content: "God has always treated me as family, whether I deserved it or not."
tags: ["family", "grace", "identity", "god", "love"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.TREATED AS FAMILY",
    alias: "Thought: Treated As Family",
    parent: "topic.GRACE",
    tags: ['family', 'grace', 'identity', 'god', 'love'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TREATED AS FAMILY",
    ctype: "THOUGHT",
    en_title: "Treated As Family",
    en_content: "God has always treated me as family, whether I deserved it or not.",
    es_title: "Tratado Como Familia",
    es_content: "Dios siempre me ha tratado como familia, ya sea que lo mereciera o no.",
    fr_title: "Traité Comme un Membre de la Famille",
    fr_content: "Dieu m'a toujours traité comme un membre de la famille, que je le mérite ou non.",
    hi_title: "परिवार की तरह व्यवहार",
    hi_content: "परमेश्वर ने हमेशा मेरे साथ परिवार की तरह व्यवहार किया है, चाहे मैं इसके योग्य था या नहीं।",
    zh_title: "Bèi dàng zuò jiā rén",
    zh_content: "Wú lùn wǒ shì fǒu zhí dé, Shàng dì zǒng shì bǎ wǒ dàng zuò jiā rén duì dài."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TREATED AS FAMILY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->TREATED AS FAMILY"
RETURN t, parent;
```
