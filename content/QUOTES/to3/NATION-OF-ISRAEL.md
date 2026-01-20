---
name: quote.NATION_OF_ISRAEL
alias: "Quote: Quote: NATION OF ISRAEL"
type: QUOTE
parent: topic.POLITICAL-SCIENCE
tags:
- nation
- israel
- earthly
- spiritual
- prophecy
neo4j: true
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NATION_OF_ISRAEL",
    alias: "Quote: Quote: NATION OF ISRAEL",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["nation", "israel", "earthly", "spiritual", "prophecy"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NATION_OF_ISRAEL",
    en_title: "Quote: NATION OF ISRAEL",
    en_content: "The Bible makes a crucial distinction between the Earthly, physical Nation of Israel, which is temporary and the SPIRITUAL Nation of Israel, which is Eternal; nothing about the Gospel or Biblical prophecy makes sense without this truth."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NATION_OF_ISRAEL"})
MATCH (c:CONTENT {name: "content.NATION_OF_ISRAEL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NATION_OF_ISRAEL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.POLITICAL-SCIENCE"})
MATCH (child:QUOTE {name: "quote.NATION_OF_ISRAEL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.POLITICAL-SCIENCE->NATION_OF_ISRAEL"}]->(child);

```
