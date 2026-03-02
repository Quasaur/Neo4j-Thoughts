---
type: QUOTE
name: "quote.REINVENT"
alias: "Quote: Quote: REINVENT"
parent: "topic.GRACE"
en_content: "It would be completely unnecessary (and a waste of time) for me to try to accomplish what God has already done for me"
tags: ["gift", "grace", "accomplish", "effort", "duplicate"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.REINVENT",
    alias: "Quote: Quote: REINVENT",
    parent: "topic.GRACE",
    tags: ["gift", "grace", "accomplish", "effort", "duplicate"],
    source: "'The Traveler's Oasis, Book One'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.REINVENT",
    en_title: "Quote: REINVENT",
    en_content: "It would be completely unnecessary (and a waste of time) for me to try to accomplish what God has already done for me"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.REINVENT"})
MATCH (c:CONTENT {name: "content.REINVENT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.REINVENT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.REINVENT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->REINVENT"}]->(child);

```
