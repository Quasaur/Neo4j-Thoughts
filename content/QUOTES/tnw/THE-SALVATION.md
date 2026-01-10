---
name: quote.THE_SALVATION
alias: "Quote: Quote: THE SALVATION"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- theonly
- life
- way
- truth
- jesuschrist
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_SALVATION",
    alias: "Quote: Quote: THE SALVATION",
    parent: "topic.THE-GOSPEL",
    tags: ["theonly", "life", "way", "truth", "jesuschrist"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_SALVATION",
    en_title: "Quote: THE SALVATION",
    en_content: "THERE IS NO SALVATION APART FROM JESUS. Let me put this another way: JESUS **IS** THE SALVATION GOD THE FATHER IS OFFERING YOU, as opposed to a set of deeds you must accomplish or words you must say to 'receive' Salvation from Jesus."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_SALVATION" AND c.name = "content.THE_SALVATION"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_SALVATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.THE_SALVATION"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE_SALVATION"}]->(child);

```
