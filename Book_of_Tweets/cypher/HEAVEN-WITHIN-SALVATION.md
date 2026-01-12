---
name: "thought.HEAVEN WITHIN SALVATION"
alias: "Thought: Heaven Within Salvation"
type: THOUGHT
en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you."
parent: "topic.GRACE"
tags:
- salvation
- heaven
- transformation
- grace
- presence
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.HEAVEN WITHIN SALVATION",
    alias: "Thought: Heaven Within Salvation",
    parent: "topic.GRACE",
    tags: ['salvation', 'heaven', 'transformation', 'grace', 'presence'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HEAVEN WITHIN SALVATION",
    en_title: "Heaven Within Salvation",
    en_content: "The objective of Salvation is not to get you into Heaven, but to get Heaven into you.",
    es_title: "El Cielo Dentro de la Salvación",
    es_content: "El objetivo de la Salvación no es llevarte al Cielo, sino traer el Cielo dentro de ti.",
    fr_title: "Le Ciel Dans le Salut",
    fr_content: "L'objectif du Salut n'est pas de vous amener au Ciel, mais d'amener le Ciel en vous.",
    hi_title: "मोक्ष के भीतर स्वर्ग",
    hi_content: "मोक्ष का उद्देश्य आपको स्वर्ग में ले जाना नहीं है, बल्कि स्वर्ग को आप के भीतर लाना है।",
    zh_title: "Jiù'ēn zhī zhōng de tiāntáng",
    zh_content: "Jiù'ēn de mùdì bùshì ràng nǐ jìnrù tiāntáng, ér shì ràng tiāntáng jìnrù nǐ de nèixīn."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEAVEN WITHIN SALVATION" AND c.name = "content.HEAVEN WITHIN SALVATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVEN WITHIN SALVATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.HEAVEN WITHIN SALVATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >HEAVEN WITHIN SALVATION" }]->(child);
```
