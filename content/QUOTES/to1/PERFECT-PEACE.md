---
name: quote.PERFECT_PEACE
alias: "Quote: Quote: PERFECT PEACE"
type: QUOTE
parent: topic.GRACE
tags:
- peace
- perfect
- grace
- holiness
- love
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PERFECT_PEACE",
    alias: "Quote: Quote: PERFECT PEACE",
    parent: "topic.GRACE",
    tags: ["peace", "perfect", "grace", "holiness", "love"],
    source: "'The Traveler's Oasis, Book One'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-One-ebook/dp/B00Y43B2OC)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PERFECT_PEACE",
    en_title: "Quote: PERFECT PEACE",
    en_content: "Every cell in my body relaxed in Perfect Peace. Every fear was vanquished. And that's why my body collapsed like a rag doll to the floor on that stage in front of all those people."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.PERFECT_PEACE" AND c.name = "content.PERFECT_PEACE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PERFECT_PEACE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.PERFECT_PEACE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->PERFECT_PEACE"}]->(child);

```
