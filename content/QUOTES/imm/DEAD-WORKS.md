---
name: quote.DEAD_WORKS
alias: "Quote: Quote: DEAD WORKS"
type: QUOTE
parent: topic.RELIGION
tags:
- sinner
- obedience
- deadspirit
- works
- filthyrags
neo4j: true
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.DEAD_WORKS",
    alias: "Quote: Quote: DEAD WORKS",
    parent: "topic.RELIGION",
    tags: ["sinner", "obedience", "deadspirit", "works", "filthyrags"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.DEAD_WORKS",
    en_title: "Quote: DEAD WORKS",
    en_content: "The obedience of the sinner CANNOT BE ACCEPTED by GOD because since the sinner is spiritually dead THEIR OBEDIENCE IS DEAD AS WELL."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.DEAD_WORKS" AND c.name = "content.DEAD_WORKS"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.DEAD_WORKS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.RELIGION" AND child.name = "quote.DEAD_WORKS"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->DEAD_WORKS"}]->(child);

```
