---
name: "thought.DEFINE FAITH PERSUASION"
alias: "Thought: Define Faith Persuasion"
type: THOUGHT
en_content: "Faith is not me persuading God to keep His Promises, but God persuading me that He is watching over His Word to perform It."
parent: "topic.FAITH"
tags:
- faith
- persuasion
- promises
- god
- truth
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013c)
CREATE (t:THOUGHT {
    name: "thought.DEFINE FAITH PERSUASION",
    alias: "Thought: Define Faith Persuasion",
    parent: "topic.FAITH",
    tags: ['faith', 'persuasion', 'promises', 'god', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEFINE FAITH PERSUASION",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE FAITH PERSUASION" AND c.name = "content.DEFINE FAITH PERSUASION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE FAITH PERSUASION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DEFINE FAITH PERSUASION"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >DEFINE FAITH PERSUASION" }]->(child);
```
