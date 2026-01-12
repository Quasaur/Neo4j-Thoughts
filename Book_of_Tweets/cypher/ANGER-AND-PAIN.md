---
name: "thought.ANGER AND PAIN"
alias: "Thought: Anger And Pain"
type: THOUGHT
en_content: "Anger as a first response is often indicative of an underlying issue...that issue usually being pain."
parent: "topic.PSYCHOLOGY"
tags:
- anger
- pain
- psychology
- response
- character
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012b)
CREATE (t:THOUGHT {
    name: "thought.ANGER AND PAIN",
    alias: "Thought: Anger And Pain",
    parent: "topic.PSYCHOLOGY",
    tags: ['anger', 'pain', 'psychology', 'response', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANGER AND PAIN",
    en_title: "Anger And Pain",
    en_content: "Anger as a first response is often indicative of an underlying issue...that issue usually being pain.",
    es_title: "Ira y Dolor",
    es_content: "La ira como primera respuesta suele ser indicativa de un problema subyacente... ese problema suele ser el dolor.",
    fr_title: "Colère et Douleur",
    fr_content: "La colère en première réponse est souvent révélatrice d'un problème sous-jacent... ce problème étant généralement la douleur.",
    hi_title: "क्रोध और पीड़ा",
    hi_content: "पहली प्रतिक्रिया के रूप में क्रोध अक्सर एक अंतर्निहित मुद्दे का संकेत होता है... वह मुद्दा आमतौर पर पीड़ा होती है।",
    zh_title: "Fènnù yǔ tòngkǔ",
    zh_content: "Fènnù zuòwéi dì yī fǎnyìng tōngcháng biǎomíng cúnzài qiánzài wèntí... gāi wèntí tōngcháng shì tòngkǔ."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANGER AND PAIN" AND c.name = "content.ANGER AND PAIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANGER AND PAIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ANGER AND PAIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >ANGER AND PAIN" }]->(child);
```
