---
type: THOUGHT
name: "thought.RESULTS"
alias: "Thought: Results"
parent: "topic.PSYCHOLOGY"
tags: ["gun_violence", "mass_shootings", "gunlaws", "nra", "uscongress"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.RESULTS",
    alias: "Thought: Results",
    parent: "topic.PSYCHOLOGY",
    tags: ["gun_violence", "mass_shootings", "gunlaws", "nra", "uscongress"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.RESULTS",
    ctype: "THOUGHT",
    en_title: "Results",
    en_content: "",
    es_title: "RESULTADOS",
    es_content: "Los resultados hablan por sí solos: la NRA y el Congreso de los Estados Unidos quieren que nos MATREMOS UNOS A OTROS... para su beneficio y a nuestra costa.",
    fr_title: "RÉSULTATS",
    fr_content: "Les résultats parlent d’eux-mêmes : la NRA et le Congrès américain veulent que nous nous entretuions… pour leur profit et à nos dépens.",
    hi_title: "परिणाम",
    hi_content: "परिणाम स्वयं बोलते हैं: एनआरए और अमेरिकी कांग्रेस चाहते हैं कि हम एक-दूसरे को मार डालें...अपने लाभ के लिए और अपने खर्च पर।",
    zh_title: "jié guǒ",
    zh_content: "jié guǒ bù yán ér yù ： quán guó bù qiāng xié huì hé měi guó guó huì xī wàng wǒ men hù xiāng cán shā …… wèi le tā men de lì yì ， ér wǒ men què fù chū dài jià 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RESULTS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->RESULTS"
RETURN t, parent;
```
