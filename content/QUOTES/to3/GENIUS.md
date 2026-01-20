---
name: quote.GENIUS
alias: "Quote: Quote: GENIUS"
type: QUOTE
parent: topic.UNDERSTANDING
tags:
- gift
- grace
- accomplish
- effort
- duplicate
neo4j: true
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.GENIUS",
    alias: "Quote: Quote: GENIUS",
    parent: "topic.UNDERSTANDING",
    tags: ["gift", "grace", "accomplish", "effort", "duplicate"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.GENIUS",
    en_title: "Quote: GENIUS",
    en_content: "Genius, like patience or temperance, is a SPIRITUAL attribute that can be acquired at any point in the life by either the Sovereignty of God or by simply asking God for it."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.GENIUS"})
MATCH (c:CONTENT {name: "content.GENIUS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GENIUS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MATCH (child:QUOTE {name: "quote.GENIUS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.UNDERSTANDING->GENIUS"}]->(child);

```
