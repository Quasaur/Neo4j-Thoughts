---
type: THOUGHT
name: "thought.PERSECUTION"
alias: "Thought: Persecution"
parent: "topic.RELIGION"
tags: ["persecution", "christianity", "original", "authentic", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
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
 es_title: "PERSECUCIÓN",
 fr_title: "PERSÉCUTION",
 hi_title: "उत्पीड़न",
 zh_title: "pò hài",
    en_content: "",
 es_content: "En la mayor parte del mundo el cristianismo es perseguido vigorosamente.
En los países donde NO se persigue, la razón es porque ESA VERSIÓN DEL CRISTIANISMO NO VALE LA PENA PERSEGUIR.",
 fr_content: "Dans la majeure partie du monde, le christianisme est vigoureusement persécuté.
Dans les pays où il n’est PAS persécuté, la raison est que CETTE VERSION DU CHRISTIANISME NE VAUT PAS LA PERSÉCUTION.",
 hi_content: "विश्व के अधिकांश देशों में ईसाई धर्म पर जोर-शोर से अत्याचार किया जाता है।
जिन देशों में इसे सताया नहीं जाता, इसका कारण यह है कि ईसाई धर्म का वह संस्करण सताए जाने लायक नहीं है।",
 zh_content: "zài shì jiè dà bù fèn dì qū ， jī dū jiào shòu dào yán zhòng pò hài 。
 zài méi yǒu shòu dào pò hài de guó jiā ， yuán yīn shì nà ge bǎn běn de jī dū jiào bù zhí dé pò hài 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PERSECUTION" AND c.name = "content.PERSECUTION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.PERSECUTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.PERSECUTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->PERSECUTION"}]->(child);
```