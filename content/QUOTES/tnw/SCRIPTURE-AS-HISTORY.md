---
name: quote.SCRIPTURE_AS_HISTORY
alias: "Quote: Quote: SCRIPTURE AS HISTORY"
type: QUOTE
parent: topic.THE-BIBLE
tags:
- bible
- research
- reliability
- holyscripture
- accuracy
neo4j: true
ptopic: "[[topic-THE-BIBLE]]"
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SCRIPTURE_AS_HISTORY",
    alias: "Quote: Quote: SCRIPTURE AS HISTORY",
    parent: "topic.THE-BIBLE",
    tags: ["bible", "research", "reliability", "holyscripture", "accuracy"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SCRIPTURE_AS_HISTORY",
    en_title: "Quote: SCRIPTURE AS HISTORY",
    en_content: "The Bible is the most accurate ancient library of its kind, and 1,500 years of so-called 'higher criticism' has not proven otherwise. Rather, the reliability and reputation of the Holy Scriptures has only increased with the continuous examination of Their contents."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SCRIPTURE_AS_HISTORY"})
MATCH (c:CONTENT {name: "content.SCRIPTURE_AS_HISTORY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SCRIPTURE_AS_HISTORY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-BIBLE"})
MATCH (child:QUOTE {name: "quote.SCRIPTURE_AS_HISTORY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-BIBLE->SCRIPTURE_AS_HISTORY"}]->(child);

```
