---
type: THOUGHT
name: "thought.SUNS ENERGY CORE"
alias: "Thought: Suns Energy Core"
parent: "topic.ASTROPHYSICS"
en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!"
tags: ["science", "sun", "energy", "creation", "time"]
ptopic: "[[topic-ASTROPHYSICS]]"
level: 5
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SUNS ENERGY CORE",
    alias: "Thought: Suns Energy Core",
    parent: "topic.ASTROPHYSICS",
    tags: ['science', 'sun', 'energy', 'creation', 'time'],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SUNS ENERGY CORE",
    ctype: "THOUGHT",
    en_title: "Thought: Suns Energy Core",
    en_content: "Energy generated in the Sun's core takes a million years to reach its surface: God is great!",
    es_title: "Pensamiento: Núcleo de energía del sol",
    es_content: "La energía generada en el núcleo del Sol tarda un millón de años en llegar a su superficie: ¡Dios es grande!",
    fr_title: "Pensée : le noyau énergétique du soleil",
    fr_content: "L'énergie générée dans le noyau du Soleil met un million d'années à atteindre sa surface : Dieu est grand !",
    hi_title: "विचार: सूर्य ऊर्जा कोर",
    hi_content: "सूर्य के केंद्र में उत्पन्न ऊर्जा को उसकी सतह तक पहुंचने में एक मिलियन वर्ष लगते हैं: परमेश्वर महान है!",
    zh_title: "xiǎng fǎ : tài yáng néng yuán hé xīn",
    zh_content: "tài yáng hé xīn chǎn shēng de néng liàng xū yào yì bǎi wàn nián cái néng dào dá qí biǎo miàn : shàng dì shì wěi dà de !"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SUNS ENERGY CORE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ASTROPHYSICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ASTROPHYSICS->SUNS ENERGY CORE"
RETURN t, parent;
```
