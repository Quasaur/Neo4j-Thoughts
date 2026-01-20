---
name: passage.MAN_OF_VIOLENCE
alias: "Passage: MAN OF VIOLENCE"
type: PASSAGE
parent: topic.EVIL
tags:
- violent
- devious
- abomination
- upright
- confidence
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.MAN_OF_VIOLENCE",
    alias: "Passage: MAN OF VIOLENCE",
    parent: "topic.EVIL",
    tags: ["violent", "devious", "abomination", "upright", "confidence"],
    source: "'Proverbs 3:31,32'",
    sortedsource: "'Proverbs 03:31-32'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A31-32&version=ESV)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.MAN_OF_VIOLENCE",
    en_title: "MAN OF VIOLENCE",
    en_content: "Do not envy a man of violence"
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.MAN_OF_VIOLENCE"})
MATCH (c:CONTENT {name: "content.MAN_OF_VIOLENCE"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.MAN_OF_VIOLENCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.MAN_OF_VIOLENCE"})
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.EVIL->MAN_OF_VIOLENCE"}]->(child);

```
