---
type: QUOTE
name: "quote.CHOSEN"
alias: "Quote: Quote: CHOSEN"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "Contrary to popular American religious legend that passes for sound Christian doctrine, the choice that COUNTS towards your ultimate eternal fate and mine is not our decisions but GOD's (John 15:16)."
tags: ["chosen", "god", "sovereignty", "jesus_christ", "eternity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHOSEN",
    alias: "Quote: Quote: CHOSEN",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["chosen", "god", "sovereignty", "jesus_christ", "eternity"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHOSEN",
    ctype: "QUOTE",
    en_title: "Quote: CHOSEN",
    en_content: "Contrary to popular American religious legend that passes for sound Christian doctrine, the choice that COUNTS towards your ultimate eternal fate and mine is not our decisions but GOD's (John 15:16)."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.CHOSEN"})
MATCH (c:CONTENT {name: "content.CHOSEN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHOSEN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.CHOSEN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->CHOSEN"}]->(child);

```
