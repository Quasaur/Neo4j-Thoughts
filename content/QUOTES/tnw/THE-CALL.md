---
name: quote.THE_CALL
alias: "Quote: Quote: THE CALL"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- preaching
- goodnews
- gladtidings
- command
- repentance
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_CALL",
    alias: "Quote: Quote: THE CALL",
    parent: "topic.THE-GOSPEL",
    tags: ["preaching", "goodnews", "gladtidings", "command", "repentance"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_CALL",
    en_title: "Quote: THE CALL",
    en_content: "That being said, for the last two thousand years GOD has put out a call to every nation, tribe, tongue and people on the face of the planet to turn to His Only-Begotten Son Jesus Christ for the forgiveness of ALL SIN--past, present and future--and to receive The Gift of The Holy Spirit of GOD and embark on the transcendent experience of That Priceless Treasure: a Sinless, Endless Life!"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_CALL"})
MATCH (c:CONTENT {name: "content.THE_CALL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_CALL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.THE_CALL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE_CALL"}]->(child);

```
