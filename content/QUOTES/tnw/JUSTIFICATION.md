---
name: quote.JUSTIFICATION
alias: "Quote: Quote: JUSTIFICATION"
type: QUOTE
parent: topic.GRACE
tags:
- just
- legal
- grace
- jesuschrist
- adquited
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.JUSTIFICATION",
    alias: "Quote: Quote: JUSTIFICATION",
    parent: "topic.GRACE",
    tags: ["just", "legal", "grace", "jesuschrist", "adquited"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.JUSTIFICATION",
    en_title: "Quote: JUSTIFICATION",
    en_content: "Oh My GOD! GOD is justifying the ungodly: that is, He is DECLARING THE UNGODLY LEGALLY JUST for Christ's Sake!! This has nothing to do with feelings, but WHAT YOU BELIEVE IN YOUR HEART!!! If you believe in your heart that what was done to Christ in the garden, in the Sanhedrin, before Herod, before Pilate, in the Praetorium and on the Cross was done for YOU, GOD considers you as just as Christ is EVEN THOUGH YOU ARE NOT!!!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.JUSTIFICATION" AND c.name = "content.JUSTIFICATION"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.JUSTIFICATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.JUSTIFICATION"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->JUSTIFICATION"}]->(child);

```
