---
name: quote.HEIR_OF_GOD!
alias: "Quote: Quote: HEIR OF GOD!"
type: QUOTE
parent: topic.THE-GOSPEL
ptopic: "[[topic-THE-GOSPEL]]"
tags:
- heir
- adoption
- son
- daughter
- jesuschrist
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HEIR_OF_GOD!",
    alias: "Quote: Quote: HEIR OF GOD!",
    parent: "topic.THE-GOSPEL",
    tags: ["heir", "adoption", "son", "daughter", "jesuschrist"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HEIR_OF_GOD!",
    en_title: "Quote: HEIR OF GOD!",
    en_content: "Thankfully, GOD has looked upon your situation with compassion and is not only offering you an escape from His Wrath, but a priceless opportunity TO BECOME HIS HEIR!!! All the 'heavy lifting' has been done for you, yet you must set your heart to follow Your Creator (GOD The Word, incarnated as Jesus the Messiah) back to the Father of all spirits and NOT LOOK BACK on the familiar life you were born into."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HEIR_OF_GOD!"})
MATCH (c:CONTENT {name: "content.HEIR_OF_GOD!"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HEIR_OF_GOD!"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.HEIR_OF_GOD!"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->HEIR_OF_GOD!"}]->(child);

```
