---
name: quote.FULL_ASSURANCE
alias: "Quote: Quote: FULL ASSURANCE"
type: QUOTE
parent: topic.GRACE
tags:
- knowing
- confidence
- guarantee
- holyspirit
- divinewitness
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FULL_ASSURANCE",
    alias: "Quote: Quote: FULL ASSURANCE",
    parent: "topic.GRACE",
    tags: ["knowing", "confidence", "guarantee", "holyspirit", "divinewitness"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FULL_ASSURANCE",
    en_title: "Quote: FULL ASSURANCE",
    en_content: "i know that KNOWING that you're going to be Saved from the Wrath of GOD is declared heresy by the Roman Catholic Church; if you STUDY A RELIABLE TRANSLATION OF THE BIBLE, however, you will see that GOD wants you to be assured and confident of your eternal destiny ([1 John 5:13-15](https://www.biblegateway.com/passage/?search=1+John+5%3A13-15&version=KJV))"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FULL_ASSURANCE"})
MATCH (c:CONTENT {name: "content.FULL_ASSURANCE"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FULL_ASSURANCE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.FULL_ASSURANCE"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->FULL_ASSURANCE"}]->(child);

```
