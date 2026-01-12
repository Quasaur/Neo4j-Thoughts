---
name: "thought.DEFINE FAITH WILL"
alias: "Thought: Define Faith Will"
type: THOUGHT
en_content: "New Definition of Faith: KNOWING God's Will for me in every situation."
parent: "topic.FAITH"
tags:
- faith
- will
- god
- knowledge
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Feb-2014)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH WILL",
    alias: "Thought: Define Faith Will",
    parent: "topic.FAITH",
    tags: ['faith', 'will', 'god', 'knowledge'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH WILL",
    en_title: "Define Faith Will",
    en_content: "New Definition of Faith: KNOWING God's Will for me in every situation.",
    es_title: "Definir Fe Voluntad",
    es_content: "Nueva Definición de Fe: CONOCER la Voluntad de Dios para mí en toda situación.",
    fr_title: "Définir la Foi Volonté",
    fr_content: "Nouvelle Définition de la Foi : CONNAÎTRE la Volonté de Dieu pour moi dans chaque situation.",
    hi_title: "विश्वास इच्छा को परिभाषित करें",
    hi_content: "विश्वास की नई परिभाषा: हर स्थिति में मेरे लिए भगवान की इच्छा जानना।",
    zh_title: "Dìngyì xìnxīn yìzhì",
    zh_content: "Xìnxīn de xīn dìngyì: Zài měi gè qíngkuàng xià dōuzhī shàngdì duì wǒ de yìzhì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE FAITH WILL" AND c.name = "content.DEFINE FAITH WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE FAITH WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DEFINE FAITH WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE FAITH WILL" }]->(child);
```
