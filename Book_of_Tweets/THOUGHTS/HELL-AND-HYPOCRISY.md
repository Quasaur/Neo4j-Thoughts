---
name: "thought.HELL AND HYPOCRISY"
alias: "Thought: Hell And Hypocrisy"
type: THOUGHT
en_content: "If I send you to Hell, it's guaranteed that I will be following you shortly."
parent: "topic.MORALITY"
tags:
- judgment
- hypocrisy
- hell
- morality
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.HELL AND HYPOCRISY",
    alias: "Thought: Hell And Hypocrisy",
    parent: "topic.MORALITY",
    tags: ['judgment', 'hypocrisy', 'hell', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HELL AND HYPOCRISY",
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

MATCH (t:THOUGHT {name: "thought.HELL AND HYPOCRISY"})
MATCH (c:CONTENT {name: "content.HELL AND HYPOCRISY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.HELL AND HYPOCRISY" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.HELL AND HYPOCRISY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY->HELL AND HYPOCRISY" }]->(child);
```
