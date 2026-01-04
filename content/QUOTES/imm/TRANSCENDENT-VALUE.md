---
name: quote.TRANSCENDENT_VALUE
alias: "Quote: Quote: TRANSCENDENT VALUE"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- gospel
- promise
- jesuschrist
- value
- precious
neo4j: true
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.TRANSCENDENT_VALUE",
    alias: "Quote: Quote: TRANSCENDENT VALUE",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "promise", "jesuschrist", "value", "precious"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRANSCENDENT_VALUE",
    en_title: "Quote: TRANSCENDENT VALUE",
    en_content: "The promise of the Gospel is that GOD The Father gives us Christ, Who is of TRANSCENDENT VALUE to Him; and in so doing we become as valuable to GOD as Christ is!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.TRANSCENDENT_VALUE" AND c.name = "content.TRANSCENDENT_VALUE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.TRANSCENDENT_VALUE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.TRANSCENDENT_VALUE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->TRANSCENDENT_VALUE"}]->(child);

```
