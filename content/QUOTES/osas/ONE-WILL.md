---
name: quote.ONE_WILL
alias: "Quote: Quote: ONE WILL"
type: QUOTE
parent: topic.DIVINE-SOVEREIGNTY
tags:
- light
- eternity
- onewill
- deity
- sovereignty
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ONE_WILL",
    alias: "Quote: Quote: ONE WILL",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["light", "eternity", "onewill", "deity", "sovereignty"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ONE_WILL",
    en_title: "Quote: ONE WILL",
    en_content: "Precious Reader, I have experienced The Light of Eternity saturating my being (The Traveler's Oasis: Book One, Chapter 18) and i can tell you that THERE IS ONLY ONE WILL THAT HAS EVER AND WILL EVER EXIST!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.ONE_WILL" AND c.name = "content.ONE_WILL"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ONE_WILL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "quote.ONE_WILL"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->ONE_WILL"}]->(child);

```
