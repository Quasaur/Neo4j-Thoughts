---
type: THOUGHT
name: "thought.HELL AND HYPOCRISY"
alias: "Thought: Hell And Hypocrisy"
parent: "topic.MORALITY"
en_content: "If I send you to Hell, it's guaranteed that I will be following you shortly."
tags: ["judgment", "hypocrisy", "hell", "morality", "character"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011b)
CREATE (t:THOUGHT {    name: "thought.HELL AND HYPOCRISY",
    alias: "Thought: Hell And Hypocrisy",
    parent: "topic.MORALITY",
    tags: ['judgment', 'hypocrisy', 'hell', 'morality', 'character'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.HELL AND HYPOCRISY",
    ctype: "THOUGHT",
    en_title: "Hell And Hypocrisy",
    en_content: "If I send you to Hell, it's guaranteed that I will be following you shortly.",
    es_title: "El Infierno y la Hipocresía",
    es_content: "Si te envío al Infierno, es garantizado que te estaré siguiendo en breve.",
    fr_title: "L'Enfer et l'Hypocrisie",
    fr_content: "Si je t'envoie en Enfer, il est garanti que je te suivrai sous peu.",
    hi_title: "नरक और पाखंड",
    hi_content: "यदि मैं तुम्हें नरक भेजूं, तो यह निश्चित है कि मैं शीघ्र ही तुम्हारे पीछे आऊंगा।",
    zh_title: "Dìyù yǔ Wěishàn",
    zh_content: "Rúguǒ wǒ sòng nǐ qù dìyù, kěn dìng de shì wǒ huì hěn kuài gēnzhe nǐ qù."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HELL AND HYPOCRISY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->HELL AND HYPOCRISY"
RETURN t, parent;
```
