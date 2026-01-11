---
name: "thought.PROSPERITY_NOW"
alias: "Thought: PROSPERITY NOW"
type: THOUGHT
parent: topic.RELIGION
tags:
- prosperity
- faith
- prayer
- supplication
- sorcery
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PROSPERITY_NOW",
    alias: "Thought: PROSPERITY NOW",
    parent: "topic.RELIGION",
    tags: ["prosperity", "faith", "prayer", "supplication", "sorcery"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PROSPERITY_NOW",
    en_title: "PROSPERITY NOW",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PROSPERITY_NOW" AND c.name = "content.PROSPERITY_NOW"
MERGE (t)-[:HAS_CONTENT {name: "edge.PROSPERITY_NOW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.PROSPERITY_NOW"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.RELIGION->PROSPERITY_NOW"}]->(child);
```
