---
type: PASSAGE
name: "passage.THE LORD GIVES"
alias: "Passage: The Rights of God."
parent: "topic.DIVINE SOVEREIGNTY"
sortedsource: "Job 01:21"
en_content: "The Lord gave, and the Lord has taken away; blessed be the name of the Lord"
tags: ["sovereignty", "blessing", "job", "lords_name", "trust"]
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
    tags: ["sovereignty", "blessing", "job", "lords_name", "trust"],
    source: "Job 1:21",
    sortedsource: "Job 01:21",
    biblelink: "https://www.biblegateway.com/passage/?search=Job%201%3A21&version=ESV",
    level: 2
})

CREATE (c:CONTENT {
    name: "content.THE LORD GIVES",
    ctype: "PASSAGE",
    en_title: "Passage: The Rights of God.",
    en_content: "The Lord gave, and the Lord has taken away; blessed be the name of the Lord",
    es_title: "Pasaje: Los derechos de Dios.",
    es_content: "El Señor dio, y el Señor quitó; bendito sea el nombre del señor",
    fr_title: "Passage : Les droits de Dieu.",
    fr_content: "Le Seigneur a donné, et le Seigneur a repris ; béni soit le nom du Seigneur",
    hi_title: "परिच्छेद: ईश्वर के अधिकार।",
    hi_content: "यहोवा ने दिया, और यहोवा ने ही ले लिया; प्रभु के नाम की रहमत बरसे!",
    zh_title: "duàn luò : shàng dì de quán lì .",
    zh_content: "shǎng cì de shì yē hé huá , shōu qǔ de yě shì yē hé huá ; zhǔ de míng shì yīng dāng chēng sòng de !"
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
