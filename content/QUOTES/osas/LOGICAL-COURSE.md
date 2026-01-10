---
name: quote.LOGICAL_COURSE
alias: "Quote: Quote: LOGICAL COURSE"
type: QUOTE
parent: topic.FAITH
tags:
- logic
- action
- faith
- creator
- understanding
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LOGICAL_COURSE",
    alias: "Quote: Quote: LOGICAL COURSE",
    parent: "topic.FAITH",
    tags: ["logic", "action", "faith", "creator", "understanding"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LOGICAL_COURSE",
    en_title: "Quote: LOGICAL COURSE",
    en_content: "The logical course of action for an ignorant creature (and all creatures are ignorant to varying degrees) is to place its total faith in its Creator Who knows and understands all."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.LOGICAL_COURSE" AND c.name = "content.LOGICAL_COURSE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LOGICAL_COURSE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.FAITH" AND child.name = "quote.LOGICAL_COURSE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->LOGICAL_COURSE"}]->(child);

```
