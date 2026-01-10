---
name: quote.THE_VALUE_OF_FAITH
alias: "Quote: Quote: THE VALUE OF FAITH"
type: QUOTE
parent: topic.FAITH
ptopic: "[[topic-FAITH]]"
tags:
- faith
- value
- worth
- target
- object
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_VALUE_OF_FAITH",
    alias: "Quote: Quote: THE VALUE OF FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "value", "worth", "target", "object"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_VALUE_OF_FAITH",
    en_title: "Quote: THE VALUE OF FAITH",
    en_content: "Faith is only as potent and valuable (or, only as REAL) as the idea, object or person in/upon which that faith is placed."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_VALUE_OF_FAITH" AND c.name = "content.THE_VALUE_OF_FAITH"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_VALUE_OF_FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.FAITH" AND child.name = "quote.THE_VALUE_OF_FAITH"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->THE_VALUE_OF_FAITH"}]->(child);

```
