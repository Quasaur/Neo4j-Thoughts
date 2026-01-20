---
name: quote.SPOKEN_ACTS
alias: "Quote: Quote: SPOKEN ACTS"
type: QUOTE
parent: topic.LINGUISTICS
tags:
- spoken
- words
- idle
- acts
- accountable
neo4j: true
ptopic: "[[topic-LINGUISTICS]]"
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SPOKEN_ACTS",
    alias: "Quote: Quote: SPOKEN ACTS",
    parent: "topic.LINGUISTICS",
    tags: ["spoken", "words", "idle", "acts", "accountable"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SPOKEN_ACTS",
    en_title: "Quote: SPOKEN ACTS",
    en_content: "Spoken words are human acts which are recorded in Heaven meticulously."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.SPOKEN_ACTS"})
MATCH (c:CONTENT {name: "content.SPOKEN_ACTS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SPOKEN_ACTS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.LINGUISTICS"})
MATCH (child:QUOTE {name: "quote.SPOKEN_ACTS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.LINGUISTICS->SPOKEN_ACTS"}]->(child);

```
