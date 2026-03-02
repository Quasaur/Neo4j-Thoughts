---
type: QUOTE
name: "quote.POLITICAL_CHRIST"
alias: "Quote: Quote: POLITICAL CHRIST"
parent: "topic.POLITICAL-SCIENCE"
en_content: "I state that not only is Jesus' Authority spiritual, but political and economic as well."
tags: ["jesus_christ", "authority", "political", "spiritual", "economical"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.POLITICAL_CHRIST",
    alias: "Quote: Quote: POLITICAL CHRIST",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["jesus_christ", "authority", "political", "spiritual", "economical"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.POLITICAL_CHRIST",
    ctype: "QUOTE",
    en_title: "Quote: POLITICAL CHRIST",
    en_content: "I state that not only is Jesus' Authority spiritual, but political and economic as well."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.POLITICAL_CHRIST"})
MATCH (c:CONTENT {name: "content.POLITICAL_CHRIST"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.POLITICAL_CHRIST"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (child:QUOTE {name: "quote.POLITICAL_CHRIST"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL-SCIENCE->POLITICAL_CHRIST"}]->(child);

```
