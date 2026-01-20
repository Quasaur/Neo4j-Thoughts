---
name: quote.THE_TEN_COMMANDMENTS
alias: "Quote: Quote: THE TEN COMMANDMENTS"
type: QUOTE
parent: topic.LAW
tags:
- peace
- perfect
- grace
- holiness
- love
neo4j: true
ptopic: "[[topic-LAW]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_TEN_COMMANDMENTS",
    alias: "Quote: Quote: THE TEN COMMANDMENTS",
    parent: "topic.LAW",
    tags: ["peace", "perfect", "grace", "holiness", "love"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_TEN_COMMANDMENTS",
    en_title: "Quote: THE TEN COMMANDMENTS",
    en_content: "God places an INESTIMABLE VALUE upon the Ten Commandments; and it deeply concerns me that so many of today's Christians take NO TIME to familiarize themselves with any of the first five books of the Bible which clearly identify the One True God in no uncertain terms."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_TEN_COMMANDMENTS"})
MATCH (c:CONTENT {name: "content.THE_TEN_COMMANDMENTS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_TEN_COMMANDMENTS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.LAW"})
MATCH (child:QUOTE {name: "quote.THE_TEN_COMMANDMENTS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LAW->THE_TEN_COMMANDMENTS"}]->(child);

```
