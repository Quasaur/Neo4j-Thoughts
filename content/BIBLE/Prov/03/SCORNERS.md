---
name: passage.SCORNERS
alias: "Passage: SCORNERS"
type: PASSAGE
parent: topic.EVIL
tags:
- scorners
- scornful
- humble
- gift
- favor
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.SCORNERS",
    alias: "Passage: SCORNERS",
    parent: "topic.EVIL",
    tags: ["scorners", "scornful", "humble", "gift", "favor"],
    source: "'Proverbs 3:34'",
    sortedsource: "'Proverbs 03:34'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A34&version=ESV)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SCORNERS",
    en_title: "SCORNERS",
    en_content: "Toward the scorners He [The LORD] is scornful,"
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.SCORNERS"})
MATCH (c:CONTENT {name: "content.SCORNERS"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.SCORNERS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.SCORNERS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->SCORNERS"}]->(child);

```
