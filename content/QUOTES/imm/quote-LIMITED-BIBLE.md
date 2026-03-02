---
type: QUOTE
name: "quote.LIMITED_BIBLE"
alias: "Quote: Quote: LIMITED BIBLE"
parent: "topic.THE-BIBLE"
en_content: "The Holy Bible does NOT tell us all there is to know about GOD! The Bible was inspired by GOD for a very specific purpose: to give the saint everything needful to be saved from the Lake of Fire—and therefore from the power of sin."
tags: ["scriptures", "bible", "uncomprehensive", "purpose", "objective"]
ptopic: "[[topic-THE-BIBLE]]"
level: 5
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LIMITED_BIBLE",
    alias: "Quote: Quote: LIMITED BIBLE",
    parent: "topic.THE-BIBLE",
    tags: ["scriptures", "bible", "uncomprehensive", "purpose", "objective"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LIMITED_BIBLE",
    ctype: "QUOTE",
    en_title: "Quote: LIMITED BIBLE",
    en_content: "The Holy Bible does NOT tell us all there is to know about GOD! The Bible was inspired by GOD for a very specific purpose: to give the saint everything needful to be saved from the Lake of Fire—and therefore from the power of sin."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.LIMITED_BIBLE"})
MATCH (c:CONTENT {name: "content.LIMITED_BIBLE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LIMITED_BIBLE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-BIBLE"})
MATCH (child:QUOTE {name: "quote.LIMITED_BIBLE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-BIBLE->LIMITED_BIBLE"}]->(child);

```
