---
name: quote.FOREKNOWN
alias: "Quote: Quote: FOREKNOWN"
type: QUOTE
parent: topic.DIVINE-SOVEREIGNTY
tags:
- foreknowledge
- god
- intimacy
- jesuschrist
- eternity
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FOREKNOWN",
    alias: "Quote: Quote: FOREKNOWN",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["foreknowledge", "god", "intimacy", "jesuschrist", "eternity"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FOREKNOWN",
    en_title: "Quote: FOREKNOWN",
    en_content: "To save you from the coming Wrath GOD must KNOW you."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.FOREKNOWN" AND c.name = "content.FOREKNOWN"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FOREKNOWN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "quote.FOREKNOWN"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->FOREKNOWN"}]->(child);

```
