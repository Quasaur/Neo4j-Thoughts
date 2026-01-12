---
name: "thought.HUMILITY OF CREATION"
alias: "Thought: Humility Of Creation"
type: THOUGHT
en_content: "It was The Supreme Act of Humility for God, Who doesn't need anything, to create something!"
parent: "topic.THE GODHEAD"
tags:
- humility
- creation
- god
- majesty
- necessity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.HUMILITY OF CREATION",
    alias: "Thought: Humility Of Creation",
    parent: "topic.THE GODHEAD",
    tags: ['humility', 'creation', 'god', 'majesty', 'necessity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.HUMILITY OF CREATION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMILITY OF CREATION" AND c.name = "content.HUMILITY OF CREATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMILITY OF CREATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.HUMILITY OF CREATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >HUMILITY OF CREATION" }]->(child);
```
