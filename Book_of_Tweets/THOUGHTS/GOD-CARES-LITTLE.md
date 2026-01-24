---
name: "thought.GOD CARES LITTLE"
alias: "Thought: God Cares Little"
type: THOUGHT
en_content: "God cares about the little people. He made the big people to care for the little people."
parent: "topic.THE GODHEAD"
tags:
- compassion
- little_people
- care
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.GOD CARES LITTLE",
    alias: "Thought: God Cares Little",
    parent: "topic.THE GODHEAD",
    tags: ['compassion', 'little_people', 'care', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD CARES LITTLE",
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

MATCH (t:THOUGHT {name: "thought.GOD CARES LITTLE"})
MATCH (c:CONTENT {name: "content.GOD CARES LITTLE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD CARES LITTLE" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.GOD CARES LITTLE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->GOD CARES LITTLE" }]->(child);
```
