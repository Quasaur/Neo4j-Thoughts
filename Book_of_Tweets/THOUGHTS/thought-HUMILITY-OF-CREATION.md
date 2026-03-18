---
type: THOUGHT
name: "thought.HUMILITY OF CREATION"
alias: "Thought: Humility Of Creation"
parent: "topic.THE GODHEAD"
en_content: "It was The Supreme Act of Humility for God, Who doesn't need anything, to create something!"
tags: ["humility", "creation", "god", "majesty", "necessity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011c)
CREATE (t:THOUGHT {    name: "thought.HUMILITY OF CREATION",
    alias: "Thought: Humility Of Creation",
    parent: "topic.THE GODHEAD",
    tags: ['humility', 'creation', 'god', 'majesty', 'necessity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.HUMILITY OF CREATION",
    ctype: "THOUGHT",
    en_title: "Humility Of Creation",
    en_content: "It was The Supreme Act of Humility for God, Who doesn't need anything, to create something!",
    es_title: "Humildad de la Creación",
    es_content: "¡Fue El Acto Supremo de Humildad para Dios, Quien no necesita nada, crear algo!",
    fr_title: "Humilité de la Création",
    fr_content: "Ce fut L'Acte Suprême d'Humilité pour Dieu, Qui n'a besoin de rien, de créer quelque chose !",
    hi_title: "सृष्टि की विनम्रता",
    hi_content: "यह परमेश्वर के लिए परम विनम्रता का कार्य था, जिसे किसी चीज़ की आवश्यकता नहीं है, कुछ सृजित करना!",
    zh_title: "Chuàngzào de Qiānbēi",
    zh_content: "Duìyú bù xūyào rènhé dōngxi de Shàngdì lái shuō, chuàngzào mǒuwù shì Zhìgāo de Qiānbēi Xíngwéi!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMILITY OF CREATION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->HUMILITY OF CREATION"
RETURN t, parent;
```
