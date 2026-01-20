---
name: quote.CESSATION_OF_LABOR
alias: "Quote: Quote: CESSATION OF LABOR"
type: QUOTE
parent: topic.GRACE
tags:
- inchrist
- byfaith
- soul
- rest
- peace
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CESSATION_OF_LABOR",
    alias: "Quote: Quote: CESSATION OF LABOR",
    parent: "topic.GRACE",
    tags: ["inchrist", "byfaith", "soul", "rest", "peace"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CESSATION_OF_LABOR",
    en_title: "Quote: CESSATION OF LABOR",
    en_content: "Upon entering by faith into Christ Jesus, the soul CEASES FROM ITS OWN LABOR, just as God did fro His. There is Peace; endless, refreshing, soothing, loving, empowering PEACE."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CESSATION_OF_LABOR"})
MATCH (c:CONTENT {name: "content.CESSATION_OF_LABOR"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CESSATION_OF_LABOR"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.CESSATION_OF_LABOR"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->CESSATION_OF_LABOR"}]->(child);

```
