---
name: quote.THE_BOOK_OF_LIFE
alias: "Quote: Quote: THE BOOK OF LIFE"
type: QUOTE
parent: topic.DIVINE-SOVEREIGNTY
tags:
- lamboflgod
- lakeoffire
- bookoflife
- immunity
- fearless
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_BOOK_OF_LIFE",
    alias: "Quote: Quote: THE BOOK OF LIFE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["lamboflgod", "lakeoffire", "bookoflife", "immunity", "fearless"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_BOOK_OF_LIFE",
    en_title: "Quote: THE BOOK OF LIFE",
    en_content: "As long as your name is written in the Lamb’s Book of LIFE, YOU HAVE NOTHING TO WORRY ABOUT WHATSOEVER; the Lake of Fire can do you no harm."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_BOOK_OF_LIFE" AND c.name = "content.THE_BOOK_OF_LIFE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_BOOK_OF_LIFE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "quote.THE_BOOK_OF_LIFE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->THE_BOOK_OF_LIFE"}]->(child);

```
