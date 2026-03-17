---
type: THOUGHT
name: "thought.ESSENCE OF JOY"
alias: "Thought: Essence Of Joy"
parent: "topic.ATTITUDE"
en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I."
tags: ["joy", "god", "majesty", "discovery", "attitude"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ESSENCE OF JOY",
    alias: "Thought: Essence Of Joy",
    parent: "topic.ATTITUDE",
    tags: ['joy', 'god', 'majesty', 'discovery', 'attitude'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ESSENCE OF JOY",
    ctype: "THOUGHT",
    en_title: "Essence Of Joy",
    en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I.",
    es_title: "Esencia del Gozo",
    es_content: "La esencia del Gozo es descubrir que Dios es más maravilloso, más grande y más importante que yo.",
    fr_title: "Essence de la Joie",
    fr_content: "L'essence de la Joie est de découvrir que Dieu est plus merveilleux, plus grand et plus important que moi.",
    hi_title: "आनंद का सार",
    hi_content: "आनंद का सार यह खोजना है कि परमेश्वर मुझसे कहीं अधिक अद्भुत, महान और महत्वपूर्ण है।",
    zh_title: "Kuàilè de Běnzhì",
    zh_content: "Kuàilè de běnzhì jiùshì fāxiàn Shàngdì bǐ wǒ gèng qímiào, gèng wěidà, gèng zhòngyào."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ESSENCE OF JOY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->ESSENCE OF JOY"
RETURN t, parent;
```
