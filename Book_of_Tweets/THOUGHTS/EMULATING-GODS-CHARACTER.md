---
name: "thought.EMULATING GODS CHARACTER"
alias: "Thought: Emulating Gods Character"
type: THOUGHT
en_content: "What kind of person is God? The kind I've always admired and desired to emulate."
parent: "topic.THE GODHEAD"
tags:
- character
- emulation
- admiration
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2012b)
CREATE (t:THOUGHT {
    name: "thought.EMULATING GODS CHARACTER",
    alias: "Thought: Emulating Gods Character",
    parent: "topic.THE GODHEAD",
    tags: ['character', 'emulation', 'admiration', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EMULATING GODS CHARACTER",
    en_title: "Emulating Gods Character",
    en_content: "What kind of person is God? The kind I've always admired and desired to emulate.",
    es_title: "Emulando el Carácter de Dios",
    es_content: "¿Qué tipo de persona es Dios? El tipo que siempre he admirado y deseado emular.",
    fr_title: "Imiter le Caractère de Dieu",
    fr_content: "Quel genre de personne est Dieu ? Le genre que j'ai toujours admiré et désiré imiter.",
    hi_title: "परमेश्वर के चरित्र का अनुकरण करना",
    hi_content: "परमेश्वर कैसा व्यक्ति है? वैसा जिसकी मैंने हमेशा प्रशंसा की है और जिसका अनुकरण करने की इच्छा की है।",
    zh_title: "mófǎng shàngdì de pǐngé",
    zh_content: "shàngdì shì shénme yàng de rén? jiùshì wǒ yīzhí qīnpèi bìng kěwàng mófǎng de nà zhǒng rén."
});

MATCH (t:THOUGHT {name: "thought.EMULATING GODS CHARACTER"})
MATCH (c:CONTENT {name: "content.EMULATING GODS CHARACTER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EMULATING GODS CHARACTER" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.EMULATING GODS CHARACTER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >EMULATING GODS CHARACTER" }]->(child);
```
