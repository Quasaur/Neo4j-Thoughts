---
type: PASSAGE
name: "passage.NEIGHBORS"
alias: "Passage: Neighbors"
parent: "topic.SOCIOLOGY"
en_content: "Do not plan evil against your neighbor,"
tags: ["scheme", "neighbor", "innocent", "contention", "motive"]
ptopic: "[[topic-SOCIOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.NEIGHBORS",
    parent: "topic.SOCIOLOGY",
    alias: "Passage: Neighbors",
    tags: ["scheme", "neighbor", "innocent", "contention", "motive"],
    source: "'Proverbs 3:29,30'",
    sortedsource: "'Proverbs 03:29-30'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A29-30&version=ESV)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.NEIGHBORS",
    ctype: "PASSAGE",
    en_title: "Neighbors",
    en_content: "Do not plan evil against your neighbor,",
 es_title: "VECINOS",
 es_content: "No planees el mal contra tu prójimo,",
 fr_title: "VOISINS",
 fr_content: "Ne planifie pas de mal contre ton prochain,",
 hi_title: "पड़ोसी",
 hi_content: "अपने पड़ोसी के विरुद्ध बुरी योजना न बनाओ,",
 zh_title: "lín jū",
 zh_content: "bù kě móu hài lín shè ，",


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.NEIGHBORS"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.SOCIOLOGY"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.SOCIOLOGY->NEIGHBORS"
RETURN b, parent;
```
