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
    en_content: "For the faithlessness of the naive will kill them, and the complacency of fools will destroy them."
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.FAITHLESSNESS"})
MATCH (c:CONTENT {name: "content.FAITHLESSNESS"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.FAITHLESSNESS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.FAITHLESSNESS"})
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.EVIL->FAITHLESSNESS"}]->(child);

```
