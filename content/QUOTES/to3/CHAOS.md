---
name: quote.CHAOS
alias: "Quote: Quote: CHAOS"
type: QUOTE
parent: topic.PSYCHOLOGY
tags:
- chaos
- disorder
- fear
- perception
- delusion
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHAOS",
    alias: "Quote: Quote: CHAOS",
    parent: "topic.PSYCHOLOGY",
    tags: ["chaos", "disorder", "fear", "perception", "delusion"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHAOS",
    en_title: "Quote: CHAOS",
    en_content: "We fear Chaos above little else and, consciously or subconsciously, are constantly trying to create order where there may actually be none."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.CHAOS" AND c.name = "content.CHAOS"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHAOS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "quote.CHAOS"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.PSYCHOLOGY->CHAOS"}]->(child);

```
