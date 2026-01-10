---
name: quote.HIS_TOOL
alias: "Quote: Quote: HIS TOOL"
type: QUOTE
parent: topic.EVIL
tags:
- knowing
- confidence
- guarantee
- holyspirit
- divinewitness
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HIS_TOOL",
    alias: "Quote: Quote: HIS TOOL",
    parent: "topic.EVIL",
    tags: ["knowing", "confidence", "guarantee", "holyspirit", "divinewitness"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HIS_TOOL",
    en_title: "Quote: HIS TOOL",
    en_content: "The Truth is this: a small cabal of individuals rule the world; their master is the Devil ([1 John 5:19](https://www.biblegateway.com/passage/?search=1+John+5%3A19&version=ESV)) and his Masters are the GODHEAD. Evil is a tool in the Hand of a Holy GOD, used to accomplish His Good Purpose ([Genesis 50:20](https://www.biblegateway.com/passage/?search=Genesis+50%3A20&version=ESV); [Romans 8:28](https://www.biblegateway.com/passage/?search=Romans+8%3A28&version=ESV))."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.HIS_TOOL" AND c.name = "content.HIS_TOOL"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HIS_TOOL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.EVIL" AND child.name = "quote.HIS_TOOL"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->HIS_TOOL"}]->(child);

```
