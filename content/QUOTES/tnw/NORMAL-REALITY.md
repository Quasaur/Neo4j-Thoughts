---
name: quote.NORMAL-REALITY
alias: "Quote: Quote: NORMAL-REALITY"
type: QUOTE
parent: topic.TRUTH
tags:
- eternity
- godhead
- reality
- normal
- glory
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NORMAL-REALITY",
    alias: "Quote: Quote: NORMAL-REALITY",
    parent: "topic.TRUTH",
    tags: ["eternity", "godhead", "reality", "normal", "glory"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NORMAL-REALITY",
    en_title: "Quote: NORMAL-REALITY",
    en_content: "Other things happened, but what i most strongly desire to convey to you is that the lives we experience in this world are NOT as real as Eternity. We live in a temporary sub-reality that is the result of humanity being disconnected from our Great and Precious Heavenly Father. The experience i was granted is NORMAL REALITY...the environment we were MEANT to be born into and live our lives in!!!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.NORMAL-REALITY" AND c.name = "content.NORMAL-REALITY"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NORMAL-REALITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.TRUTH" AND child.name = "quote.NORMAL-REALITY"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.TRUTH->NORMAL-REALITY"}]->(child);

```
