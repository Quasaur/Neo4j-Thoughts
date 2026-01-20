---
name: "thought.EXPERIENCING GOD"
alias: "Thought: Experiencing God"
type: THOUGHT
en_content: "You don't want to live your entire life and die without experiencing God."
parent: "topic.SPIRITUALITY"
tags:
- experience
- god
- life
- death
- presence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.EXPERIENCING GOD",
    alias: "Thought: Experiencing God",
    parent: "topic.SPIRITUALITY",
    tags: ['experience', 'god', 'life', 'death', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EXPERIENCING GOD",
    en_title: "Experiencing God",
    en_content: "You don't want to live your entire life and die without experiencing God.",
    es_title: "Experimentando a Dios",
    es_content: "No quieres vivir toda tu vida y morir sin experimentar a Dios.",
    fr_title: "Faire l'expérience de Dieu",
    fr_content: "Tu ne veux pas vivre toute ta vie et mourir sans faire l'expérience de Dieu.",
    hi_title: "ईश्वर का अनुभव",
    hi_content: "आप अपना पूरा जीवन जीकर ईश्वर का अनुभव किए बिना मरना नहीं चाहते।",
    zh_title: "Jīnglì Shàngdì",
    zh_content: "Nǐ bù xiǎng zhěng gè rénshēng dōu méiyǒu jīnglì Shàngdì jiù sǐqù."
});

MATCH (t:THOUGHT {name: "thought.EXPERIENCING GOD"})
MATCH (c:CONTENT {name: "content.EXPERIENCING GOD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EXPERIENCING GOD" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.EXPERIENCING GOD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >EXPERIENCING GOD" }]->(child);
```
