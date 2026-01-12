---
name: "thought.GODS WILL IN ME"
alias: "Thought: Gods Will In Me"
type: THOUGHT
en_content: "I can't make God do anything; yet He effortlessly executes His Will in me without my awareness of the act."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- sovereignty
- providence
- grace
- willpower
- surrender
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.GODS WILL IN ME",
    alias: "Thought: Gods Will In Me",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['sovereignty', 'providence', 'grace', 'willpower', 'surrender'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GODS WILL IN ME",
    en_title: "Gods Will In Me",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS WILL IN ME" AND c.name = "content.GODS WILL IN ME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS WILL IN ME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.GODS WILL IN ME"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >GODS WILL IN ME" }]->(child);
```
