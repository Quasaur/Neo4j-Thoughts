---
name: quote.EVIL_IDENTIFIED
alias: "Quote: Quote: EVIL IDENTIFIED"
type: QUOTE
parent: topic.EVIL
tags:
- evil
- ungodly
- withoutgod
- humanitarian
- deadworks
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.EVIL_IDENTIFIED",
    alias: "Quote: Quote: EVIL IDENTIFIED",
    parent: "topic.EVIL",
    tags: ["evil", "ungodly", "withoutgod", "humanitarian", "deadworks"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.EVIL_IDENTIFIED",
    en_title: "Quote: EVIL IDENTIFIED",
    en_content: "Evil is not identified by works alone but by the absence of GOD in the human heart. The most altruistic soul walking the Earth today without Christ Jesus is just as damned as the most prolific serial killer."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.EVIL_IDENTIFIED" AND c.name = "content.EVIL_IDENTIFIED"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.EVIL_IDENTIFIED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.EVIL" AND child.name = "quote.EVIL_IDENTIFIED"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->EVIL_IDENTIFIED"}]->(child);

```
