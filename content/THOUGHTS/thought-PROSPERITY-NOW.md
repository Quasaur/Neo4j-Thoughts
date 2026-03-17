---
type: THOUGHT
name: "thought.PROSPERITY NOW"
alias: "Thought: Prosperity Now"
parent: "topic.RELIGION"
en_content: "If the itinerary of our lives is in our hands instead of God’s, then prayer is no longer supplication, but sorcery."
tags: ["prosperity", "faith", "prayer", "supplication", "sorcery"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PROSPERITY NOW",
    alias: "Thought: Prosperity Now",
    parent: "topic.RELIGION",
    tags: ["prosperity", "faith", "prayer", "supplication", "sorcery"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PROSPERITY NOW",
    ctype: "THOUGHT",
    en_title: "Prosperity Now",
    en_content: "If the itinerary of our lives is in our hands instead of God’s, then prayer is no longer supplication, but sorcery.",
    es_title: "PROSPERIDAD AHORA",
    es_content: "Si el itinerario de nuestra vida está en nuestras manos y no en las de Dios, entonces la oración ya no es súplica, sino brujería.",
    fr_title: "LA PROSPÉRITÉ MAINTENANT",
    fr_content: "Si l’itinéraire de notre vie est entre nos mains et non entre celles de Dieu, alors la prière n’est plus une supplication, mais une sorcellerie.",
    hi_title: "अब समृद्धि",
    hi_content: "यदि हमारे जीवन की यात्रा योजना ईश्वर के बजाय हमारे हाथों में है, तो प्रार्थना अब याचना नहीं, बल्कि जादू-टोना है।",
    zh_title: "xiàn zài de fán róng",
    zh_content: "rú guǒ wǒ men shēng mìng de xíng chéng zhǎng wò zài wǒ men ér bú shì shén shǒu zhōng ， nà me dǎo gào jiù bù zài shì kěn qiú ， ér shì wū shù 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PROSPERITY NOW"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->PROSPERITY NOW"
RETURN t, parent;
```
