---
name: quote.THE_SERVANT_KING
alias: "Quote: Quote: THE SERVANT KING"
type: QUOTE
parent: topic.ATTITUDE
tags:
- greatest
- servant
- burdenbearer
- foundation
- jesuschrist
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_SERVANT_KING",
    alias: "Quote: Quote: THE SERVANT KING",
    parent: "topic.ATTITUDE",
    tags: ["greatest", "servant", "burdenbearer", "foundation", "jesuschrist"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_SERVANT_KING",
    en_title: "Quote: THE SERVANT KING",
    en_content: "OH MY GOD!!! Here the Lord Jesus Christ distinguishes Himself from all the great men (and great thinkers) of history who have either preceded Him or came after Him! If the Claims Jesus made about Himself are true, He had at His disposal enough absolute power to bend all human society to His Will... Yet, in His First Advent, He refuses to exert a single iota of His Divine Sovereignty to shape human will or human hearts! Rather, by the Spirit of Humility, He calls, teaches and persuades us by means of deeds the lowliest of slaves would be hesitant to perform!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_SERVANT_KING" AND c.name = "content.THE_SERVANT_KING"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_SERVANT_KING"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "quote.THE_SERVANT_KING"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->THE_SERVANT_KING"}]->(child);

```
