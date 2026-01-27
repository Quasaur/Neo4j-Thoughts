---
name: passage.FAITHLESSNESS
alias: "Passage: FAITHLESSNESS"
type: PASSAGE
parent: topic.EVIL
tags:
- faithlessness
- naive
- complacency
- fools
- destruction
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.FAITHLESSNESS",
    alias: "Passage: FAITHLESSNESS",
    parent: "topic.EVIL",
    tags: ["faithlessness", "naive", "complacency", "fools", "destruction"],
    source: "'Proverbs 1:32'",
    sortedsource: "'Proverbs 01:32'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+1%3A32&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FAITHLESSNESS",
    en_title: "FAITHLESSNESS",
    en_content: "For the faithlessness of the naive will kill them, and the complacency of fools will destroy them.",
 es_title: "FIDELIDAD",
 es_content: "Porque la infidelidad de los ingenuos los matará, y la complacencia de los necios los destruirá.",
 fr_title: "INFIDÉLITÉ",
 fr_content: "Car l'infidélité des naïfs les tuera, et la complaisance des insensés les détruira.",
 hi_title: "बेवफ़ाई",
 hi_content: "क्योंकि भोले-भाले लोगों की निष्ठा उन्हें मार डालेगी, और मूर्खों की शालीनता उन्हें नष्ट कर देगी।",
 zh_title: "bù zhōng",
 zh_content: "yīn wèi tiān zhēn zhě de bù xìn jiāng shā sǐ tā men ， yú zhě de zì mǎn jiāng huǐ miè tā men 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.FAITHLESSNESS"})
MATCH (c:CONTENT {name: "content.FAITHLESSNESS"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.FAITHLESSNESS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.FAITHLESSNESS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->FAITHLESSNESS"}]->(child);

```
