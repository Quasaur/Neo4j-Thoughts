---
type: PASSAGE
name: "passage.FATE OF THE WICKED"
alias: "Passage: Fate of the Wicked"
parent: "topic.EVIL"
sortedsource: "Proverbs 02:22"
en_content: "But the wicked will be eliminated from the land, And the treacherous will be torn away from it."
tags: ["wicked", "eliminated", "treacherous", "torn", "land"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// 1. Create the Passage and Content nodes
// Using 'b' and 'c' as variables to keep them in memory
CREATE (b:PASSAGE {
    name: "passage.FATE OF THE WICKED",
    parent: "topic.EVIL",
    alias: "Passage: Fate of the Wicked",
    tags: ["wicked", "eliminated", "treacherous", "torn", "land"],
    source: "Proverbs 2:22",
    sortedsource: "Proverbs 02:22",
    biblelink: "https://www.biblegateway.com/passage/?search=proverbs+2%3A22&version=NASB",
    level: 4
})

CREATE (c:CONTENT {
    
    
    name: "content.FATE OF THE WICKED",
    ctype: "PASSAGE",
    en_title: "Passage: Fate of the Wicked",
    en_content: "But the wicked will be eliminated from the land, And the treacherous will be torn away from it.",
 es_title: "Pasaje: El destino de los malvados",
 es_content: "Pero los impíos serán eliminados de la tierra, y los traidores serán arrancados de ella.",
 fr_title: "Passage : Le destin des méchants",
 fr_content: "Mais les méchants seront éliminés du pays, Et les perfides en seront arrachés.",
 hi_title: "परिच्छेद: दुष्टों का भाग्य",
 hi_content: "परन्तु दुष्ट लोग देश में से नाश किए जाएंगे, और विश्वासघाती उस में से नाश किए जाएंगे।",
 zh_title: "duàn luò : è rén de mìng yùn",
 zh_content: "dàn è rén bì cóng dì shàng bèi xiāo miè ， jiān zhà rén bì cóng dì shàng bèi bá chú 。"
})

// 2. Link Content to Passage using the variables 'b' and 'c'
MERGE (b)-[r1:HAS_CONTENT]->(c)
ON CREATE SET r1.name = "p.edge.FATE OF THE WICKED"

// 3. Pass 'b' forward, find the Parent Topic, and link them
WITH b
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_PASSAGE]->(b)
ON CREATE SET r2.name = "p.edge.EVIL->FATE OF THE WICKED"
RETURN b, parent;
```
