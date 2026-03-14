---
type: PASSAGE
name: "passage.SCORNERS"
alias: "Passage: Scorners"
parent: "topic.EVIL"
en_content: "Toward the scorners He [The LORD] is scornful,"
tags: ["scorners", "scornful", "humble", "gift", "favor"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.SCORNERS",
    parent: "topic.EVIL",
    alias: "Passage: Scorners",
    tags: ["scorners", "scornful", "humble", "gift", "favor"],
    source: "'Proverbs 3:34'",
    sortedsource: "'Proverbs 03:34'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A34&version=ESV)",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.SCORNERS",
    ctype: "PASSAGE",
    en_title: "Scorners",
    en_content: "Toward the scorners He [The LORD] is scornful,",
 es_title: "SCORNERADORES",
 es_content: "Con los escarnecedores Él [Jehová] es escarnecedor,",
 fr_title: "Les moqueurs",
 fr_content: "Il [l'Éternel] se moque des moqueurs,",
 hi_title: "उपहास करने वाले",
 hi_content: "वह [प्रभु] ठट्ठा करनेवालों के प्रति तिरस्कार करता है,",
 zh_title: "miè shì zhě",
 zh_content: "tā ［ yē hé huá ］ miǎo shì xiè màn de rén ，",


})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.SCORNERS"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.EVIL->SCORNERS"
RETURN b, parent;
```
