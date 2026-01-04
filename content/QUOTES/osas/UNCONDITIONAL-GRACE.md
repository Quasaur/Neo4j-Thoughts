---
name: quote.UNCONDITIONAL_GRACE
alias: "Quote: Quote: UNCONDITIONAL GRACE"
type: QUOTE
parent: topic.GRACE
tags:
- saved
- understanding
- darkness
- past
- forgotten
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNCONDITIONAL_GRACE",
    alias: "Quote: Quote: UNCONDITIONAL GRACE",
    parent: "topic.GRACE",
    tags: ["saved", "understanding", "darkness", "past", "forgotten"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL_GRACE",
    en_title: "Quote: UNCONDITIONAL GRACE",
    en_content: "The Purpose of the Gospel is to bring fallen numanity into The Fellowship of The Godhead. And since the Fellowship of The Godhead is Itself unconditional, The Gospel of Grace must also be unconditional."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.UNCONDITIONAL_GRACE" AND c.name = "content.UNCONDITIONAL_GRACE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNCONDITIONAL_GRACE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.UNCONDITIONAL_GRACE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->UNCONDITIONAL_GRACE"}]->(child);

```
