---
type: PASSAGE
name: "passage.MAN OF VIOLENCE"
alias: "Passage: Man of Violence"
parent: "topic.EVIL"
en_content: "Do not envy a man of violence"
tags: ["violent", "devious", "abomination", "upright", "confidence"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.MAN OF VIOLENCE",
    alias: "Passage: Man of Violence",
    parent: "topic.EVIL",
    tags: ["violent", "devious", "abomination", "upright", "confidence"],
    source: "'Proverbs 3:31,32'",
    sortedsource: "'Proverbs 03:31-32'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A31-32&version=ESV)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.MAN OF VIOLENCE",
    ctype: "PASSAGE",
    en_title: "Man of Violence",
    en_content: "Do not envy a man of violence",
 es_title: "HOMBRE DE VIOLENCIA",
 es_content: "No envidies a un hombre violento",
 fr_title: "HOMME DE VIOLENCE",
 fr_content: "N'enviez pas un homme violent",
 hi_title: "हिंसा का आदमी",
 hi_content: "हिंसा करने वाले व्यक्ति से ईर्ष्या न करें",
 zh_title: "bào lì zhī rén",
 zh_content: "bú yào jí dù yǒu bào lì qīng xiàng de rén",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.MAN OF VIOLENCE"})
MATCH (c:CONTENT {name: "content.MAN OF VIOLENCE"})
MERGE (b)-[:HAS_CONTENT {name: "p.edge.MAN OF VIOLENCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.MAN OF VIOLENCE"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->MAN OF VIOLENCE"}]->(child);

```
