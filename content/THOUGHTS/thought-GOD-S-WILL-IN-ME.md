---
type: THOUGHT
name: "thought.GOD'S WILL IN ME"
alias: "Thought: God's Will In Me"
parent: "topic.GOD'S WILL"
en_content: "I can't make God do anything; yet He effortlessly executes His Will in me without my awareness of the act."
tags: ["sovereignty", "providence", "grace", "willpower", "surrender"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD'S WILL IN ME",
    alias: "Thought: God's Will In Me",
    parent: "topic.GOD'S WILL",
    tags: ['sovereignty', 'providence', 'grace', 'willpower', 'surrender'],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD'S WILL IN ME",
    ctype: "THOUGHT",
    en_title: "God's Will In Me",
    en_content: "I can't make God do anything; yet He effortlessly executes His Will in me without my awareness of the act.",
    es_title: "La Voluntad de Dios en Mí",
    es_content: "No puedo hacer que Dios haga nada; sin embargo, Él ejecuta sin esfuerzo Su Voluntad en mí sin que yo tenga conciencia del acto.",
    fr_title: "La Volonté de Dieu en Moi",
    fr_content: "Je ne peux pas faire faire quoi que ce soit à Dieu ; pourtant Il exécute sans effort Sa Volonté en moi sans que j'aie conscience de l'acte.",
    hi_title: "मुझमें परमेश्वर की इच्छा",
    hi_content: "मैं परमेश्वर से कुछ भी करवा नहीं सकता; फिर भी वह सहजता से मुझमें अपनी इच्छा का क्रियान्वयन करता है बिना मेरे इस कृत्य के प्रति जागरूक हुए।",
    zh_title: "Shén de Yìzhì zài Wǒ Xīnzhōng",
    zh_content: "Wǒ bùnéng ràng Shén zuò rènhé shì; rán'ér Tā háobùfèilì de zài wǒ xīnzhōng zhíxíng Tā de Yìzhì, ér wǒ què duì zhè xíngwéi háowú zhījué."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD'S WILL IN ME"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->GOD'S WILL IN ME"
RETURN t, parent;
```
