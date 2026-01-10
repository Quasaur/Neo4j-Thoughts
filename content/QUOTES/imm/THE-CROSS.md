---
name: quote.THE_CROSS
alias: "Quote: Quote: THE CROSS"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- gospel
- power
- jesuschrist
- redemption
- sanctification
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_CROSS",
    alias: "Quote: Quote: THE CROSS",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "power", "jesuschrist", "redemption", "sanctification"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_CROSS",
    en_title: "Quote: THE CROSS",
    en_content: "The Power of the Gospel is The Cross of Jesus Christ. The “magic” of The Cross is that GOD loved us so unconditionally and so deeply that He spared neither Himself nor us the pain and agony necessary to provide us a complete delivery from the power, penalty and—most important—the love of and need for sin."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_CROSS" AND c.name = "content.THE_CROSS"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_CROSS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.THE_CROSS"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE_CROSS"}]->(child);

```
