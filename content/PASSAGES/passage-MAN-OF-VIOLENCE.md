---
type: PASSAGE
name: "passage.MAN OF VIOLENCE"
alias: "Passage: Man of Violence"
parent: "topic.EVIL"
sortedsource: "Proverbs 03:31-32"
en_content: "Do not envy a man of violence, and do not choose any of his ways."
tags: ["violent", "devious", "abomination", "upright", "confidence"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.MAN OF VIOLENCE",
    parent: "topic.EVIL",
    alias: "Passage: Man of Violence",
    tags: ["violent", "devious", "abomination", "upright", "confidence"],
    source: "Proverbs 3:31,32",
    sortedsource: "Proverbs 03:31-32",
    biblelink: "https://www.biblegateway.com/passage/?search=Proverbs%203%3A31-32&version=ESV",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.MAN OF VIOLENCE",
    ctype: "PASSAGE",
    en_title: "Passage: Man of Violence",
    en_content: "Do not envy a man of violence, and do not choose any of his ways.",
 es_title: "Pasaje: Hombre de violencia",
 es_content: "No envidies al hombre violento, ni elijas ninguno de sus caminos.",
 fr_title: "Passage : Homme de violence",
 fr_content: "N'enviez pas un homme violent et ne choisissez aucune de ses voies.",
 hi_title: "परिच्छेद: हिंसा का आदमी",
 hi_content: "हिंसा करने वाले मनुष्य से डाह न करना, और न उसका कोई मार्ग चुनना।",
 zh_title: "duàn luò : bào lì zhī rén",
 zh_content: "bú yào jí dù shī bào de rén , yě bú yào xuǎn zé tā de dào lù ."
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
