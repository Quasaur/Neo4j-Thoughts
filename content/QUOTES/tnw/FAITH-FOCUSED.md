---
name: quote.FAITH-FOCUSED
alias: "Quote: Quote: FAITH-FOCUSED"
type: QUOTE
parent: topic.FAITH
tags:
- faith
- focus
- wordoffaith
- jesuschrist
- self
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FAITH-FOCUSED",
    alias: "Quote: Quote: FAITH-FOCUSED",
    parent: "topic.FAITH",
    tags: ["faith", "focus", "wordoffaith", "jesuschrist", "self"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FAITH-FOCUSED",
    en_title: "Quote: FAITH-FOCUSED",
    en_content: "Here's a hint: if you're stuck in doubt, it's because YOU'RE FOCUSED ON THE WRONG PERSON. If you're looking inward at yourself the only conclusion you can come to is 'impossible.' But if you turn your attention to Jesus and His Unconditional Love for you, your confidence in His Word (in this case Romans Chapter Six) will grow and meet the challenge of your past with the glory of your future in Christ."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.FAITH-FOCUSED" AND c.name = "content.FAITH-FOCUSED"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FAITH-FOCUSED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.FAITH" AND child.name = "quote.FAITH-FOCUSED"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->FAITH-FOCUSED"}]->(child);

```
