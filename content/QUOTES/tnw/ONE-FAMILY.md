---
name: quote.ONE_FAMILY
alias: "Quote: Quote: ONE FAMILY"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- tribe
- clan
- family
- united
- jesuschrist
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ONE_FAMILY",
    alias: "Quote: Quote: ONE FAMILY",
    parent: "topic.THE-GOSPEL",
    tags: ["tribe", "clan", "family", "united", "jesuschrist"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ONE_FAMILY",
    en_title: "Quote: ONE FAMILY",
    en_content: "GOD created the human family with the intent of filling its members with the SAME FULLNESS His Divine Family enjoys; since the advent of sin, however, humans have conspired with demons to so darken that which was designed to be glorious that the Presence of Divinity would be temporarily forced out."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.ONE_FAMILY" AND c.name = "content.ONE_FAMILY"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ONE_FAMILY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.ONE_FAMILY"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->ONE_FAMILY"}]->(child);

```
