---
type: PASSAGE
name: "passage.FAITHLESSNESS"
alias: "Passage: Faithlessness"
parent: "topic.EVIL"
sortedsource: "Proverbs 01:32"
en_content: "For the faithlessness of the naive will kill them, and the complacency of fools will destroy them."
tags: ["faithlessness", "naive", "complacency", "fools", "destruction"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.FAITHLESSNESS",
    parent: "topic.EVIL",
    alias: "Passage: Faithlessness",
    tags: ["faithlessness", "naive", "complacency", "fools", "destruction"],
    source: "Proverbs 1:32",
    sortedsource: "Proverbs 01:32",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs+1%3A32&version=NASB",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.FAITHLESSNESS",
    ctype: "PASSAGE",
    en_title: "Passage: Faithlessness",
    en_content: "For the faithlessness of the naive will kill them, and the complacency of fools will destroy them.",
 es_title: "Pasaje: Infidelidad",
 es_content: "Porque la infidelidad de los ingenuos los matará, y la complacencia de los necios los destruirá.",
 fr_title: "Passage : Infidélité",
 fr_content: "Car l'infidélité des naïfs les tuera, et la complaisance des insensés les détruira.",
 hi_title: "परिच्छेद: अविश्वास",
 hi_content: "क्योंकि भोले-भाले लोगों की निष्ठा उन्हें मार डालेगी, और मूर्खों की शालीनता उन्हें नष्ट कर देगी।",
 zh_title: "jīng wén : bù xìn",
 zh_content: "yīn wèi tiān zhēn zhě de bù xìn jiāng shā sǐ tā men ， yú zhě de zì mǎn jiāng huǐ miè tā men 。"
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.FAITHLESSNESS"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.EVIL->FAITHLESSNESS"
RETURN b, parent;
```
