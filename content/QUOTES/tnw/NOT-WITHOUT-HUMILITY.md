---
name: quote.NOT_WITHOUT_HUMILITY
alias: "Quote: Quote: NOT WITHOUT HUMILITY"
type: QUOTE
parent: topic.ATTITUDE
tags:
- repentance
- gift
- humble
- essential
- heart
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NOT_WITHOUT_HUMILITY",
    alias: "Quote: Quote: NOT WITHOUT HUMILITY",
    parent: "topic.ATTITUDE",
    tags: ["repentance", "gift", "humble", "essential", "heart"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NOT_WITHOUT_HUMILITY",
    en_title: "Quote: NOT WITHOUT HUMILITY",
    en_content: "What i wish to remind us all is that THERE'S NO SALVATION WITHOUT REPENTANCE AND THERE'S NO REPENTANCE WITHOUT HUMILITY."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NOT_WITHOUT_HUMILITY"})
MATCH (c:CONTENT {name: "content.NOT_WITHOUT_HUMILITY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NOT_WITHOUT_HUMILITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MATCH (child:QUOTE {name: "quote.NOT_WITHOUT_HUMILITY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->NOT_WITHOUT_HUMILITY"}]->(child);

```
