---
type: THOUGHT
name: "thought.ISLAM"
alias: "Thought: Islam"
parent: "topic.RELIGION"
tags: ["islam", "religion", "antichrist", "demonic", "deception"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ISLAM",
    alias: "Thought: Islam",
    parent: "topic.RELIGION",
    tags: ["islam", "religion", "antichrist", "demonic", "deception"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ISLAM",
    ctype: "THOUGHT",
    en_title: "Islam",
    en_content: "",
    es_title: "ISLAM",
    es_content: "NO hay armonía posible entre El Evangelio de Jesucristo (que es la única Barrera entre la humanidad y El Lago de Fuego y Azufre) y la Religión de Mahoma.",
    fr_title: "ISLAM",
    fr_content: "Il n’y a AUCUNE harmonie possible entre l’Évangile de Jésus-Christ (qui est la seule barrière entre l’humanité et l’étang de feu et de soufre) et la religion de Mahomet.",
    hi_title: "इस्लाम",
    hi_content: "ईसा मसीह के सुसमाचार (जो मानवता और आग और गंधक की झील के बीच एकमात्र बाधा है) और मोहम्मद के धर्म के बीच कोई सामंजस्य संभव नहीं है।",
    zh_title: "yī sī lán jiào",
    zh_content: "yē sū jī dū de fú yīn （ zhè shì rén lèi yǔ huǒ liú hú zhī jiān de wéi yī zhàng ài ） yǔ mù hǎn mò dé de zōng jiào zhī jiān bù kě néng yǒu hé xié 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ISLAM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->ISLAM"
RETURN t, parent;
```
