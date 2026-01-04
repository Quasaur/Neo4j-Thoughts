---
name: quote.MY_PROGRAMMING
alias: "Quote: Quote: MY PROGRAMMING"
type: QUOTE
parent: topic.PSYCHOLOGY
tags:
- programming
- brainwashing
- training
- dream
- fiction
neo4j: true
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.MY_PROGRAMMING",
    alias: "Quote: Quote: MY PROGRAMMING",
    parent: "topic.PSYCHOLOGY",
    tags: ["programming", "brainwashing", "training", "dream", "fiction"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.MY_PROGRAMMING",
    en_title: "Quote: MY PROGRAMMING",
    en_content: "In contrast, my programming was virtually complete. When my controller raised his firearm to his son's face, the well-honed logic that had so faithfully enabled me to survive numerous assignments kicked into gear with machine-like precision."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.MY_PROGRAMMING" AND c.name = "content.MY_PROGRAMMING"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.MY_PROGRAMMING"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "quote.MY_PROGRAMMING"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.PSYCHOLOGY->MY_PROGRAMMING"}]->(child);

```
