---
name: quote.CHRIST_IS_ENOUGH
alias: "Quote: Quote: CHRIST IS ENOUGH"
type: QUOTE
parent: topic.GRACE
tags:
- jesuschrist
- sufficient
- enough
- salvation
- redemption
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHRIST_IS_ENOUGH",
    alias: "Quote: Quote: CHRIST IS ENOUGH",
    parent: "topic.GRACE",
    tags: ["jesuschrist", "sufficient", "enough", "salvation", "redemption"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHRIST_IS_ENOUGH",
    en_title: "Quote: CHRIST IS ENOUGH",
    en_content: "I say to you again in the Name of The Father, Son and Holy Spirit and in the Presence of Heaven, Earth and all Creation: JESUS CHRIST IS ENOUGH to completely deliver any soul from damnation to Divine Perfection."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.CHRIST_IS_ENOUGH" AND c.name = "content.CHRIST_IS_ENOUGH"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHRIST_IS_ENOUGH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.CHRIST_IS_ENOUGH"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->CHRIST_IS_ENOUGH"}]->(child);

```
