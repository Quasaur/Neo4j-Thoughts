---
type: THOUGHT
name: "thought.ATTENTION DESIRE"
alias: "Thought: Attention Desire"
parent: "topic.ATTITUDE"
en_content: "I only want your attention when you don't want to give it to me."
tags: ["attitude", "attention", "human_nature", "desire", "pride"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ATTENTION DESIRE",
    alias: "Thought: Attention Desire",
    parent: "topic.ATTITUDE",
    tags: ["attitude", "attention", "human_nature", "desire", "pride"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATTENTION DESIRE",
    ctype: "THOUGHT",
    en_title: "Attention Desire",
    en_content: "I only want your attention when you don't want to give it to me.",
    es_title: "Deseo de Atención",
    es_content: "Solo quiero tu atención cuando no quieres dármela.",
    fr_title: "Désir d'Attention",
    fr_content: "Je ne veux ton attention que lorsque tu ne veux pas me la donner.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "मुझे केवल तभी आपका ध्यान चाहिए जब आप मुझे देना नहीं चाहते।",
    zh_title: "Kěwàng guānzhù",
    zh_content: "Wǒ zhǐ zài nǐ bù xiǎng gěi wǒ guānzhù de shíhòu cái xiǎng yào nǐ de guānzhù."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ATTENTION DESIRE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ATTENTION DESIRE"
RETURN t, parent;
```
