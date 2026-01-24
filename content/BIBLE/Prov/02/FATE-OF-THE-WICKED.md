---
name: passage.FATE_OF_THE_WICKED
alias: "Passage: FATE OF THE WICKED"
type: PASSAGE
parent: topic.EVIL
tags:
- wicked
- eliminated
- treacherous
- torn
- land
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.FATE_OF_THE_WICKED",
    alias: "Passage: FATE OF THE WICKED",
    parent: "topic.EVIL",
    tags: ["wicked", "eliminated", "treacherous", "torn", "land"],
    source: "'Proverbs 2:22'",
    sortedsource: "'Proverbs 02:22'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+2%3A22&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FATE_OF_THE_WICKED",
    en_title: "FATE OF THE WICKED",
    en_content: "But the wicked will be eliminated from the land, And the treacherous will be torn away from it."
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.FATE_OF_THE_WICKED"})
MATCH (c:CONTENT {name: "content.FATE_OF_THE_WICKED"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.FATE_OF_THE_WICKED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.FATE_OF_THE_WICKED"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->FATE_OF_THE_WICKED"}]->(child);

```
