---
name: quote.UNCONDITIONAL
alias: "Quote: Quote: UNCONDITIONAL"
type: QUOTE
parent: topic.GRACE
tags:
- gospel
- purpose
- fellowship
- godhead
- unconditional
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNCONDITIONAL",
    alias: "Quote: Quote: UNCONDITIONAL",
    parent: "topic.GRACE",
    tags: ["gospel", "purpose", "fellowship", "godhead", "unconditional"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNCONDITIONAL",
    en_title: "Quote: UNCONDITIONAL",
    en_content: "The Purpose of the Gospel is to bring fallen humanity into The Fellowship of The GODHEAD. And since the Fellowship of The GODHEAD is Itself unconditional, The Gospel of Grace must also be unconditional."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.UNCONDITIONAL" AND c.name = "content.UNCONDITIONAL"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNCONDITIONAL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.UNCONDITIONAL"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->UNCONDITIONAL"}]->(child);

```
