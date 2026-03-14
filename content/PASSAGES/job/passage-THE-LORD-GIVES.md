---
type: PASSAGE
name: "passage.THE LORD GIVES"
alias: "Passage: The Rights of God."
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "The Lord gives, and the Lord takes away. Blessed be The Name of the Lord! -- The Prophet 'Iyowb (Job)"
tags: ["sovereignty", "blessing", "jodb", "lords_name", "trust"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 't' and 'c' as variables to keep them in memory
CREATE (t:PASSAGE {
    name: "passage.THE LORD GIVES",
    parent: "topic.DIVINE SOVEREIGNTY",
    alias: "Passage: The Rights of God.",
    tags: ["sovereignty", "blessing", "jodb", "lords_name", "trust"],
    level: 2
})

CREATE (c:CONTENT {
    name: "content.THE LORD GIVES",
    ctype: "PASSAGE",
    en_title: "The Lord Gives",
    en_content: "The Lord gives. The Lord takes away. Blessed be The Name of the Lord! -- The Prophet 'Iyowb (Job)",
    es_title: "El Señor da",
    es_content: "El Señor dio y el Señor quitó; ¡bendito sea el nombre del Señor! -- El Profeta Iyowb (Job)",
    fr_title: "Le Seigneur donne",
    fr_content: "El Eterno ha dado, y el Eterno ha quitado; ¡bendito sea el nombre del Eterno! -- El Profeta Iyowb (Job)",
    hi_title: "bhagavaan deta hai",
    hi_content: "प्रभु ने दिया, प्रभु ने ले लिया। प्रभु का नाम धन्य हो! -- भविष्यद्वक्ता इय्याब (अय्यूब)",
    zh_title: "Yēhéhuá shǎngcì",
    zh_content: "shǎng cì de shì yē hé huá, shǒu huí de yě shì yē hé huá ; yē hé huá de míng shì yīng dāng chéng sòng de! -- xiān zhī yóu bó"
})

// 2. Link Content to Passage using the variables 't' and 'c'
MERGE (t)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.THE LORD GIVES"

// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(t)
ON CREATE SET r2.name = "p.edge.DIVINE SOVEREIGNTY->THE LORD GIVES"
RETURN t, parent;
```
