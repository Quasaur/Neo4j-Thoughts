---
type: THOUGHT
name: "thought.PERSECUTION"
alias: "Thought: Persecution"
parent: "topic.RELIGION"
tags: ["persecution", "christianity", "original", "authentic", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PERSECUTION",
    alias: "Thought: Persecution",
    parent: "topic.RELIGION",
    tags: ["persecution", "christianity", "original", "authentic", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PERSECUTION",
    ctype: "THOUGHT",
    en_title: "Persecution",
    en_content: "",
    es_title: "PERSECUCIÓN",
    es_content: "En la mayor parte del mundo el cristianismo es perseguido vigorosamente.
En los países donde NO se persigue, la razón es porque ESA VERSIÓN DEL CRISTIANISMO NO VALE LA PENA PERSEGUIR.",
    fr_title: "PERSÉCUTION",
    fr_content: "Dans la majeure partie du monde, le christianisme est vigoureusement persécuté.
Dans les pays où il n’est PAS persécuté, la raison est que CETTE VERSION DU CHRISTIANISME NE VAUT PAS LA PERSÉCUTION.",
    hi_title: "उत्पीड़न",
    hi_content: "विश्व के अधिकांश देशों में ईसाई धर्म पर जोर-शोर से अत्याचार किया जाता है।
जिन देशों में इसे सताया नहीं जाता, इसका कारण यह है कि ईसाई धर्म का वह संस्करण सताए जाने लायक नहीं है।",
    zh_title: "pò hài",
    zh_content: "zài shì jiè dà bù fèn dì qū ， jī dū jiào shòu dào yán zhòng pò hài 。
 zài méi yǒu shòu dào pò hài de guó jiā ， yuán yīn shì nà ge bǎn běn de jī dū jiào bù zhí dé pò hài 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PERSECUTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.RELIGION->PERSECUTION"
RETURN t, parent;
```
