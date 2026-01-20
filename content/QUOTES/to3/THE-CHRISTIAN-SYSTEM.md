---
name: quote.THE_CHRISTIAN_SYSTEM
alias: "Quote: Quote: THE CHRISTIAN SYSTEM"
type: QUOTE
parent: topic.POLITICAL-SCIENCE
tags:
- christianity
- jesuschrist
- truth
- political
- economic
neo4j: true
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_CHRISTIAN_SYSTEM",
    alias: "Quote: Quote: THE CHRISTIAN SYSTEM",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["christianity", "jesuschrist", "truth", "political", "economic"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_CHRISTIAN_SYSTEM",
    en_title: "Quote: THE CHRISTIAN SYSTEM",
    en_content: "So what is Christianity? Jesus Christ, and all Truth concerning Him IS Christianity. So by saying that Jesus Christ is a political / economic figurehead as well as a spiritual figurehead I am implying that Christianity is a political / economic system as well."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_CHRISTIAN_SYSTEM"})
MATCH (c:CONTENT {name: "content.THE_CHRISTIAN_SYSTEM"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_CHRISTIAN_SYSTEM"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (child:QUOTE {name: "quote.THE_CHRISTIAN_SYSTEM"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL-SCIENCE->THE_CHRISTIAN_SYSTEM"}]->(child);

```
