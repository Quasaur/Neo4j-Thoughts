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
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.MAN OF VIOLENCE",
    parent: "topic.EVIL",
    alias: "Passage: Man of Violence",
    tags: ["violent", "devious", "abomination", "upright", "confidence"],
    source: "'Proverbs 3:31,32'",
    sortedsource: "'Proverbs 03:31-32'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A31-32&version=ESV)",
    level: 4
})

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


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.MAN OF VIOLENCE"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.EVIL->MAN OF VIOLENCE"
RETURN b, parent;
```
