---
name: passage.OBLIGATION
alias: "Passage: OBLIGATION"
type: PASSAGE
parent: topic.MORALITY
tags:
- obligation
- due
- now
- bills
- morality
neo4j: true
ptopic: "[[topic-MORALITY]]"
level: 3
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.OBLIGATION",
    alias: "Passage: OBLIGATION",
    parent: "topic.MORALITY",
    tags: ["obligation", "due", "now", "bills", "morality"],
    source: "'Proverbs 3:27,28'",
    sortedsource: "'Proverbs 03:27-28'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A27-28&version=ESV)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.OBLIGATION",
    en_title: "OBLIGATION",
    en_content: "Do not withhold good from those to whom it is due,"
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.OBLIGATION"})
MATCH (c:CONTENT {name: "content.OBLIGATION"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.OBLIGATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:PASSAGE {name: "passage.OBLIGATION"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.MORALITY->OBLIGATION"}]->(child);

```
