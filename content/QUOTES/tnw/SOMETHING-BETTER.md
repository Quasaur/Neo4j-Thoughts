---
name: quote.SOMETHING_BETTER
alias: "Quote: Quote: SOMETHING BETTER"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- superior
- religion
- gospel
- jesuschrist
- simple
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SOMETHING_BETTER",
    alias: "Quote: Quote: SOMETHING BETTER",
    parent: "topic.THE-GOSPEL",
    tags: ["superior", "religion", "gospel", "jesuschrist", "simple"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SOMETHING_BETTER",
    en_title: "Quote: SOMETHING BETTER",
    en_content: "The Gospel (the REAL Gospel of Jesus Christ) offers Something exponentially better and more exciting than religion...Something so simple, so pure and so wonderful that even those who claim to believe the Gospel still wrestle with the thought that It might be too good to be true!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.SOMETHING_BETTER" AND c.name = "content.SOMETHING_BETTER"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SOMETHING_BETTER"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.SOMETHING_BETTER"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->SOMETHING_BETTER"}]->(child);

```
