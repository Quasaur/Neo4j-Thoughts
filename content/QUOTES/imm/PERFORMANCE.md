---
name: quote.PERFORMANCE
alias: "Quote: Quote: PERFORMANCE"
type: QUOTE
parent: topic.RELIGION
tags:
- doubt
- performance
- christ
- righteousness
- assurance
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.PERFORMANCE",
    alias: "Quote: Quote: PERFORMANCE",
    parent: "topic.RELIGION",
    tags: ["doubt", "performance", "christ", "righteousness", "assurance"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PERFORMANCE",
    en_title: "Quote: PERFORMANCE",
    en_content: "Doubt: As long as ANY PART of your Salvation is dependent upon your performance rather than Christ’s Righteousness, you can NEVER be assured of your Eternal Salvation nor of your name’s place in the Lamb’s Book of LIFE."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.PERFORMANCE"})
MATCH (c:CONTENT {name: "content.PERFORMANCE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.PERFORMANCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.PERFORMANCE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->PERFORMANCE"}]->(child);

```
