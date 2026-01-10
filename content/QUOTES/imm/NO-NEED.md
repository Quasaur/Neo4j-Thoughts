---
name: quote.NO_NEED
alias: "Quote: Quote: NO NEED"
type: QUOTE
parent: topic.WEALTH
tags:
- survive
- thrive
- needless
- money
- wisdom
neo4j: true
ptopic: "[[topic-WEALTH]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NO_NEED",
    alias: "Quote: Quote: NO NEED",
    parent: "topic.WEALTH",
    tags: ["survive", "thrive", "needless", "money", "wisdom"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NO_NEED",
    en_title: "Quote: NO NEED",
    en_content: "You do not need money to either survive or thrive in this life or the next."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.NO_NEED" AND c.name = "content.NO_NEED"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NO_NEED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.WEALTH" AND child.name = "quote.NO_NEED"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WEALTH->NO_NEED"}]->(child);

```
