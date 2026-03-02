---
type: QUOTE
name: "quote.THE_BOOK_OF_LIFE"
alias: "Quote: Quote: THE BOOK OF LIFE"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "As long as your name is written in the Lamb’s Book of LIFE, YOU HAVE NOTHING TO WORRY ABOUT WHATSOEVER; the Lake of Fire can do you no harm."
tags: ["lamb_of_god", "lake_of_fire", "book_of_life", "immunity", "fearless"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_BOOK_OF_LIFE",
    alias: "Quote: Quote: THE BOOK OF LIFE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["lamb_of_god", "lake_of_fire", "book_of_life", "immunity", "fearless"],
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
MATCH (q:QUOTE {name: "quote.THE_BOOK_OF_LIFE"})
MATCH (c:CONTENT {name: "content.THE_BOOK_OF_LIFE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_BOOK_OF_LIFE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.THE_BOOK_OF_LIFE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->THE_BOOK_OF_LIFE"}]->(child);

```
