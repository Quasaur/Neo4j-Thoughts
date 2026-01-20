---
name: quote.BANKRUPT
alias: "Quote: Quote: BANKRUPT"
type: QUOTE
parent: topic.GRACE
tags:
- offering
- sin
- shame
- failure
- holyspirit
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.BANKRUPT",
    alias: "Quote: Quote: BANKRUPT",
    parent: "topic.GRACE",
    tags: ["offering", "sin", "shame", "failure", "holyspirit"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.BANKRUPT",
    en_title: "Quote: BANKRUPT",
    en_content: "We can never be allowed to experience the Power of GOD’s Holy Spirit until we fully understand that we are absolutely bankrupt (both morally and spiritually), with nothing to offer GOD except our sin, our shame and our failure."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.BANKRUPT"})
MATCH (c:CONTENT {name: "content.BANKRUPT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.BANKRUPT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.BANKRUPT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->BANKRUPT"}]->(child);

```
