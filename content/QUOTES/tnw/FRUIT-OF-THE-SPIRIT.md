---
name: quote.FRUIT_OF_THE_SPIRIT
alias: "Quote: Quote: FRUIT OF THE SPIRIT"
type: QUOTE
parent: topic.GRACE
tags:
- works
- fruit
- flow
- livingwater
- tree
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FRUIT_OF_THE_SPIRIT",
    alias: "Quote: Quote: FRUIT OF THE SPIRIT",
    parent: "topic.GRACE",
    tags: ["works", "fruit", "flow", "livingwater", "tree"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FRUIT_OF_THE_SPIRIT",
    en_title: "Quote: FRUIT OF THE SPIRIT",
    en_content: "Notice they're not called the Works of the Spirit but the Fruit of the Spirit. The Apostle is drawing a contrast between the WORKS of the flesh and the FRUIT of the Holy Spirit of GOD...subtle yet critical. 'Works...fruit...what does it matter?' Ahhhh...it does matter, and the difference determines the destiny of billions for Heaven or Hell!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.FRUIT_OF_THE_SPIRIT" AND c.name = "content.FRUIT_OF_THE_SPIRIT"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FRUIT_OF_THE_SPIRIT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.FRUIT_OF_THE_SPIRIT"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->FRUIT_OF_THE_SPIRIT"}]->(child);

```
