---
name: passage.PROTECTION_FROM_EVIL
alias: "Passage: PROTECTION FROM EVIL"
type: PASSAGE
parent: topic.EVIL
tags:
- wisdom
- knowledge
- discretion
- understanding
- rescue
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.PROTECTION_FROM_EVIL",
    alias: "Passage: PROTECTION FROM EVIL",
    parent: "topic.EVIL",
    tags: ["wisdom", "knowledge", "discretion", "understanding", "rescue"],
    source: "'Proverbs 2:10-12'",
    sortedsource: "'Proverbs 02:10-12'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+2%3A10-12&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PROTECTION_FROM_EVIL",
    en_title: "PROTECTION FROM EVIL",
    en_content: "For wisdom will enter your heart, And knowledge will be delightful to your soul; Discretion will watch over you, Understanding will guard you, To rescue you from the way of evil, From a person who speaks perverse things;"
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.PROTECTION_FROM_EVIL"})
MATCH (c:CONTENT {name: "content.PROTECTION_FROM_EVIL"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.PROTECTION_FROM_EVIL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.PROTECTION_FROM_EVIL"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->PROTECTION_FROM_EVIL"}]->(child);

```
