---
type: PASSAGE
name: "passage.FATE OF THE WICKED"
alias: "Passage: Fate of the Wicked"
parent: "topic.EVIL"
en_content: "But the wicked will be eliminated from the land, And the treacherous will be torn away from it."
tags: ["wicked", "eliminated", "treacherous", "torn", "land"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.FATE OF THE WICKED",
    alias: "Passage: Fate of the Wicked",
    parent: "topic.EVIL",
    tags: ["wicked", "eliminated", "treacherous", "torn", "land"],
    source: "'Proverbs 2:22'",
    sortedsource: "'Proverbs 02:22'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+2%3A22&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FATE OF THE WICKED",
    ctype: "PASSAGE",
    en_title: "Fate of the Wicked",
    en_content: "But the wicked will be eliminated from the land, And the treacherous will be torn away from it.",
 es_title: "DESTINO DE LOS MALVADOS",
 es_content: "Pero los impíos serán eliminados de la tierra, y los traidores serán arrancados de ella.",
 fr_title: "LE SORT DES MÉCHANTS",
 fr_content: "Mais les méchants seront éliminés du pays, Et les perfides en seront arrachés.",
 hi_title: "दुष्टों का भाग्य",
 hi_content: "परन्तु दुष्ट लोग देश में से नाश किए जाएंगे, और विश्वासघाती उस में से नाश किए जाएंगे।",
 zh_title: "è rén de mìng yùn",
 zh_content: "dàn è rén bì cóng dì shàng bèi xiāo miè ， jiān zhà rén bì cóng dì shàng bèi bá chú 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.FATE OF THE WICKED"})
MATCH (c:CONTENT {name: "content.FATE OF THE WICKED"})
MERGE (b)-[:HAS_CONTENT {name: "p.edge.FATE OF THE WICKED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.FATE OF THE WICKED"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->FATE OF THE WICKED"}]->(child);

```
