---
name: quote.PRAYER
alias: "Quote: Quote: PRAYER"
type: QUOTE
parent: topic.WORSHIP
tags:
- pray
- real
- god
- self
- circumstance
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PRAYER",
    alias: "Quote: Quote: PRAYER",
    parent: "topic.WORSHIP",
    tags: ["pray", "real", "god", "self", "circumstance"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PRAYER",
    en_title: "Quote: PRAYER",
    en_content: "To your soul GOD BECOMES MORE REAL AND YOU (and your circumstances and situations) BECOME LESS REAL."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.PRAYER" AND c.name = "content.PRAYER"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PRAYER"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.WORSHIP" AND child.name = "quote.PRAYER"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WORSHIP->PRAYER"}]->(child);

```
