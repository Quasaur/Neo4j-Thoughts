---
name: quote.HUMILITY
alias: "Quote: Quote: HUMILITY"
type: QUOTE
parent: topic.HUMILITY
tags:
- selfimage
- bible
- god
- reservedness
- salvation
neo4j: true
ptopic: "[[topic-HUMILITY]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HUMILITY",
    alias: "Quote: Quote: HUMILITY",
    parent: "topic.HUMILITY",
    tags: ["selfimage", "bible", "god", "reservedness", "salvation"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HUMILITY",
    en_title: "Quote: HUMILITY",
    en_content: "A realistic view of ourselves in the Light of the Holy Scriptures and in the Presence of Almighty GOD is what we call HUMILITY; and without this humility Salvation is simply impossible."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HUMILITY"})
MATCH (c:CONTENT {name: "content.HUMILITY"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HUMILITY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMILITY"})
MATCH (child:QUOTE {name: "quote.HUMILITY"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMILITY->HUMILITY"}]->(child);

```
