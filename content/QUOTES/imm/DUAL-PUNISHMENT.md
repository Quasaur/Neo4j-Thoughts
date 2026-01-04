---
name: quote.DUAL_PUNISHMENT
alias: "Quote: Quote: DUAL PUNISHMENT"
type: QUOTE
parent: topic.JUSTICE
tags:
- sin
- jesuschrist
- propitiation
- substitute
- sacrifice
neo4j: true
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.DUAL_PUNISHMENT",
    alias: "Quote: Quote: DUAL PUNISHMENT",
    parent: "topic.JUSTICE",
    tags: ["sin", "jesuschrist", "propitiation", "substitute", "sacrifice"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.DUAL_PUNISHMENT",
    en_title: "Quote: DUAL PUNISHMENT",
    en_content: "It is ILLEGAL for GOD The Father to punish both you and Jesus for the same sin(s)!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.DUAL_PUNISHMENT" AND c.name = "content.DUAL_PUNISHMENT"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.DUAL_PUNISHMENT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.JUSTICE" AND child.name = "quote.DUAL_PUNISHMENT"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.JUSTICE->DUAL_PUNISHMENT"}]->(child);

```
