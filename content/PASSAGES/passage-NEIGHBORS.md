---
type: PASSAGE
name: "passage.NEIGHBORS"
alias: "Passage: Neighbors"
parent: "topic.SOCIOLOGY"
sortedsource: "Proverbs 03:29-30"
en_content: "Do not plan evil against your neighbor, who dwells trustingly beside you."
tags: ["scheme", "neighbor", "innocent", "contention", "motive"]
ptopic: "[[topic-SOCIOLOGY]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.NEIGHBORS",
    parent: "topic.SOCIOLOGY",
    alias: "Passage: Neighbors",
    tags: ["scheme", "neighbor", "innocent", "contention", "motive"],
    source: "Proverbs 3:29,30",
    sortedsource: "Proverbs 03:29-30",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A29-30&version=ESV",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.NEIGHBORS",
    ctype: "PASSAGE",
    en_title: "Passage: Neighbors",
    en_content: "Do not plan evil against your neighbor, who dwells trustingly beside you.",
 es_title: "Pasaje: Vecinos",
 es_content: "No planees el mal contra tu prójimo, que habita confiadamente a tu lado.",
 fr_title: "Passage : Voisins",
 fr_content: "Ne planifie pas de mal contre ton prochain, qui habite en toute confiance à côté de toi.",
 hi_title: "परिच्छेद: पड़ोसी",
 hi_content: "अपने पड़ोसी के विरुद्ध बुराई की योजना मत बनाओ, जो तुम्हारे साथ विश्वासपूर्वक रहता है।",
 zh_title: "duàn luò : lín jū",
 zh_content: "bú yào duì nǐ de lín jū cè huà xié è , yīn wèi tā men xìn rèn nǐ , zhù zài nǐ shēn biān ."
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
