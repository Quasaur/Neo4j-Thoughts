---
name: quote.ISLAM_DEFEATED
alias: "Quote: Quote: ISLAM DEFEATED"
type: QUOTE
parent: topic.RELIGION
tags:
- islam
- christianity
- biblical
- bible
- jesuschrist
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ISLAM_DEFEATED",
    alias: "Quote: Quote: ISLAM DEFEATED",
    parent: "topic.RELIGION",
    tags: ["islam", "christianity", "biblical", "bible", "jesuschrist"],
    source: "'Letters from God: A Work of Fiction'",
    booklink: "(https://www.amazon.com/Letters-God-Fiction-Calvin-Mitchell-ebook/dp/B01M255OZX)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ISLAM_DEFEATED",
    en_title: "Quote: ISLAM DEFEATED",
    en_content: "Biblical Christianity will defeat Islam by the same means it defeated paganism: through the Truth of the Holy Bible, the Love of Jesus Christ, and the Life of Christ lived through His followers."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ISLAM_DEFEATED"})
MATCH (c:CONTENT {name: "content.ISLAM_DEFEATED"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ISLAM_DEFEATED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.ISLAM_DEFEATED"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->ISLAM_DEFEATED"}]->(child);

```
