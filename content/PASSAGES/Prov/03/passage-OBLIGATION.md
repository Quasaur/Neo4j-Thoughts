---
type: PASSAGE
name: "passage.OBLIGATION"
alias: "Passage: Obligation"
parent: "topic.MORALITY"
en_content: "Do not withhold good from those to whom it is due,"
tags: ["obligation", "due", "now", "bills", "morality"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.OBLIGATION",
    parent: "topic.MORALITY",
    alias: "Passage: Obligation",
    tags: ["obligation", "due", "now", "bills", "morality"],
    source: "'Proverbs 3:27,28'",
    sortedsource: "'Proverbs 03:27-28'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A27-28&version=ESV)",
    level: 3
})

CREATE (c:CONTENT {
    
    
    name: "content.OBLIGATION",
    ctype: "PASSAGE",
    en_title: "Obligation",
    en_content: "Do not withhold good from those to whom it is due,",
 es_title: "OBLIGACIÓN",
 es_content: "No niegues el bien a quien es debido,",
 fr_title: "OBLIGATION",
 fr_content: "Ne refusez pas le bien à celui à qui il est dû,",
 hi_title: "दायित्व",
 hi_content: "उन लोगों से भलाई न रोको जिनका यह हक़ है,",
 zh_title: "yì wù",
 zh_content: "bú yào jù jué xiàng nà xiē yīng dé de rén xíng shàn ，",


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.OBLIGATION"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.MORALITY->OBLIGATION"
RETURN b, parent;
```
