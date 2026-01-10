---
name: quote.CHRIST_THE_END
alias: "Quote: Quote: CHRIST THE END"
type: QUOTE
parent: topic.LAW
tags:
- jesuschrist
- completion
- fulfillment
- ceremoniallaw
- oldcovenant
neo4j: true
ptopic: "[[topic-LAW]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHRIST_THE_END",
    alias: "Quote: Quote: CHRIST THE END",
    parent: "topic.LAW",
    tags: ["jesuschrist", "completion", "fulfillment", "ceremoniallaw", "oldcovenant"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHRIST_THE_END",
    en_title: "Quote: CHRIST THE END",
    en_content: "Just as Christ is the 'end' (the COMPLETION of or FULFILLMENT of) the ceremonial law of sacrifices and atonement, He is the 'end' of the Old Covenant (the Ten Commandments) itself."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.CHRIST_THE_END" AND c.name = "content.CHRIST_THE_END"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHRIST_THE_END"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.LAW" AND child.name = "quote.CHRIST_THE_END"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LAW->CHRIST_THE_END"}]->(child);

```
