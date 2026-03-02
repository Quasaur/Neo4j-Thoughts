---
type: QUOTE
name: "quote.SO_MANY_GOSPELS"
alias: "Quote: Quote: SO MANY GOSPELS"
parent: "topic.RELIGION"
en_content: "The fact is that there are many 'gospels' floating around in religious sects (both Catholic and Protestant, as well as non-Christian esoterics); most of them not really giving any glory to the Lordship of Jesus Christ nor agreeing with the doctrines handed down by those who were witnesses to His Holy Resurrection."
tags: ["gospels", "False", "religion", "doctrine", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SO_MANY_GOSPELS",
    alias: "Quote: Quote: SO MANY GOSPELS",
    parent: "topic.RELIGION",
    tags: ["gospels", "False", "religion", "doctrine", "jesus_christ"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SO_MANY_GOSPELS",
    en_title: "Quote: SO MANY GOSPELS",
    en_content: "The fact is that there are many 'gospels' floating around in religious sects (both Catholic and Protestant, as well as non-Christian esoterics); most of them not really giving any glory to the Lordship of Jesus Christ nor agreeing with the doctrines handed down by those who were witnesses to His Holy Resurrection."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SO_MANY_GOSPELS"})
MATCH (c:CONTENT {name: "content.SO_MANY_GOSPELS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SO_MANY_GOSPELS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.SO_MANY_GOSPELS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->SO_MANY_GOSPELS"}]->(child);

```
