---
name: quote.ETERNAL_LIGHT
alias: "Quote: Quote: ETERNAL LIGHT"
type: QUOTE
parent: topic.UNDERSTANDING
tags:
- saved
- understanding
- darkness
- past
- forgotten
neo4j: true
ptopic: "[[topic-UNDERSTANDING]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ETERNAL_LIGHT",
    alias: "Quote: Quote: ETERNAL LIGHT",
    parent: "topic.UNDERSTANDING",
    tags: ["saved", "understanding", "darkness", "past", "forgotten"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ETERNAL_LIGHT",
    en_title: "Quote: ETERNAL LIGHT",
    en_content: "Eventually, as saved beings, our understanding of God will reach the point where darkness will recede into the past as a faint memory."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.ETERNAL_LIGHT" AND c.name = "content.ETERNAL_LIGHT"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ETERNAL_LIGHT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.UNDERSTANDING" AND child.name = "quote.ETERNAL_LIGHT"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.UNDERSTANDING->ETERNAL_LIGHT"}]->(child);

```
