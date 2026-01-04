---
name: quote.THE_NARROW_WAY
alias: "Quote: Quote: THE NARROW WAY"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- god
- peace
- reconciliation
- selfdenial
- submission
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_NARROW_WAY",
    alias: "Quote: Quote: THE NARROW WAY",
    parent: "topic.THE-GOSPEL",
    tags: ["god", "peace", "reconciliation", "selfdenial", "submission"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_NARROW_WAY",
    en_title: "Quote: THE NARROW WAY",
    en_content: "As the only means to peace with our Creator, the Narrow Way (the Gospel) must be communicated with clarity and simplicity. Declared properly, the Narrow Way will always push me into a corner and compel me to decide against my self and for GOD. The Objective of Salvation is not to get GOD on my side, but to get me to take the side of GOD against my self!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_NARROW_WAY" AND c.name = "content.THE_NARROW_WAY"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_NARROW_WAY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.THE_NARROW_WAY"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE_NARROW_WAY"}]->(child);

```
