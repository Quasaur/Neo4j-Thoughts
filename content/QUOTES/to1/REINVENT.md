---
name: quote.REINVENT
alias: "Quote: Quote: REINVENT"
type: QUOTE
parent: topic.GRACE
tags:
- gift
- grace
- accomplish
- effort
- duplicate
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
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
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.REINVENT" AND c.name = "content.REINVENT"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.REINVENT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.REINVENT"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->REINVENT"}]->(child);

```
