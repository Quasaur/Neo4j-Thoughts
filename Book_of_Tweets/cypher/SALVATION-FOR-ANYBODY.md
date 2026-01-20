---
name: "thought.SALVATION FOR ANYBODY"
alias: "Thought: Salvation For Anybody"
type: THOUGHT
en_content: "Salvation is not for everybody, yet God can save anybody!"
parent: "topic.GRACE"
tags:
- salvation
- grace
- power
- god
- hope
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.SALVATION FOR ANYBODY",
    alias: "Thought: Salvation For Anybody",
    parent: "topic.GRACE",
    tags: ['salvation', 'grace', 'power', 'god', 'hope'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SALVATION FOR ANYBODY",
    en_title: "Salvation For Anybody",
    en_content: "Salvation is not for everybody, yet God can save anybody!",
    es_title: "Salvación Para Cualquiera",
    es_content: "La salvación no es para todos, ¡pero Dios puede salvar a cualquiera!",
    fr_title: "Salut Pour N'importe Qui",
    fr_content: "Le salut n'est pas pour tout le monde, mais Dieu peut sauver n'importe qui !",
    hi_title: "किसी के लिए भी उद्धार",
    hi_content: "उद्धार सभी के लिए नहीं है, फिर भी परमेश्वर किसी को भी बचा सकता है!",
    zh_title: "Rènhé Rén De Jiùēn",
    zh_content: "Jiùēn bùshì wèi suǒyǒu rén, dàn Shàngdì kěyǐ zhěngjiù rènhé rén!"
});

MATCH (t:THOUGHT {name: "thought.SALVATION FOR ANYBODY"})
MATCH (c:CONTENT {name: "content.SALVATION FOR ANYBODY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SALVATION FOR ANYBODY" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.SALVATION FOR ANYBODY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >SALVATION FOR ANYBODY" }]->(child);
```
