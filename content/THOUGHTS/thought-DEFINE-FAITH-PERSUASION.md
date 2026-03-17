---
type: THOUGHT
name: "thought.DEFINE FAITH PERSUASION"
alias: "Thought: Define Faith Persuasion"
parent: "topic.FAITH"
en_content: "Faith is not me persuading God to keep His Promises, but God persuading me that He is watching over His Word to perform It."
tags: ["faith", "persuasion", "promises", "god", "truth"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH PERSUASION",
    alias: "Thought: Define Faith Persuasion",
    parent: "topic.FAITH",
    tags: ['faith', 'persuasion', 'promises', 'god', 'truth'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH PERSUASION",
    ctype: "THOUGHT",
    en_title: "Define Faith Persuasion",
    en_content: "Faith is not me persuading God to keep His Promises, but God persuading me that He is watching over His Word to perform It.",
    es_title: "Definir Fe Persuasión",
    es_content: "La fe no es persuadir a Dios para que cumpla Sus Promesas, sino Dios persuadiéndome de que Él está velando sobre Su Palabra para cumplirla.",
    fr_title: "Définir la Foi Persuasion",
    fr_content: "La foi n'est pas moi persuadant Dieu de tenir Ses Promesses, mais Dieu me persuadant qu'Il veille sur Sa Parole pour l'accomplir.",
    hi_title: "विश्वास मनाने को परिभाषित करें",
    hi_content: "विश्वास यह नहीं है कि मैं भगवान को उनकी प्रतिज्ञाओं को पूरा करने के लिए मनाऊं, बल्कि भगवान मुझे यह मनाते हैं कि वे अपनी वाणी पर निगरानी कर रहे हैं ताकि उसे पूरा करें।",
    zh_title: "Dìngyì xìnxīn shuìfú",
    zh_content: "Xìnxīn bùshì wǒ shuìfú shàngdì zūnshǒu tā de nuòyán, ér shì shàngdì shuìfú wǒ tā zài zhùshì tā de huà yǐ zhíxíng tā."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DEFINE FAITH PERSUASION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->DEFINE FAITH PERSUASION"
RETURN t, parent;
```
