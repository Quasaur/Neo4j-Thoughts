---
type: THOUGHT
name: "thought.GOD CARES LITTLE"
alias: "Thought: God Cares Little"
parent: "topic.THE GODHEAD"
en_content: "God cares about the little people. He made the big people to care for the little people."
tags: ["compassion", "little_people", "care", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2012)
CREATE (t:THOUGHT {    name: "thought.GOD CARES LITTLE",
    alias: "Thought: God Cares Little",
    parent: "topic.THE GODHEAD",
    tags: ['compassion', 'little_people', 'care', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD CARES LITTLE",
    ctype: "THOUGHT",
    en_title: "God Cares Little",
    en_content: "God cares about the little people. He made the big people to care for the little people.",
    es_title: "Dios Se Preocupa por los Pequeños",
    es_content: "Dios se preocupa por la gente pequeña. Él hizo a la gente grande para cuidar de la gente pequeña.",
    fr_title: "Dieu Se Soucie des Petits",
    fr_content: "Dieu se soucie des petites gens. Il a fait les grandes gens pour prendre soin des petites gens.",
    hi_title: "परमेश्वर छोटों की चिंता करता है",
    hi_content: "परमेश्वर छोटे लोगों की चिंता करता है। उसने बड़े लोगों को छोटे लोगों की देखभाल के लिए बनाया है।",
    zh_title: "Shàngdì Guānxīn Xiǎo Rén",
    zh_content: "Shàngdì guānxīn xiǎo rén. Tā chuàngzào dà rén lái zhàogù xiǎo rén."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD CARES LITTLE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD CARES LITTLE"
RETURN t, parent;
```
