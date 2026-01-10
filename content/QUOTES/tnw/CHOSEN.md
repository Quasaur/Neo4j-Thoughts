---
name: quote.CHOSEN
alias: "Quote: Quote: CHOSEN"
type: QUOTE
parent: topic.DIVINE-SOVEREIGNTY
tags:
- chosen
- god
- sovereignty
- jesuschrist
- eternity
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHOSEN",
    alias: "Quote: Quote: CHOSEN",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["chosen", "god", "sovereignty", "jesuschrist", "eternity"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHOSEN",
    en_title: "Quote: CHOSEN",
    en_content: "Contrary to popular American religious legend that passes for sound Christian doctrine, the choice that COUNTS towards your ultimate eternal fate and mine is not our decisions but GOD's (John 15:16)."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.CHOSEN" AND c.name = "content.CHOSEN"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHOSEN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "quote.CHOSEN"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->CHOSEN"}]->(child);

```
