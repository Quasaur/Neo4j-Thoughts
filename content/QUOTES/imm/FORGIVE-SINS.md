---
name: quote.FORGIVE_SINS
alias: "Quote: Quote: FORGIVE SINS"
type: QUOTE
parent: topic.MERCY
tags:
- jesuschrist
- authority
- earth
- remission
- sins
neo4j: true
ptopic: "[[topic-MERCY]]"
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FORGIVE_SINS",
    alias: "Quote: Quote: FORGIVE SINS",
    parent: "topic.MERCY",
    tags: ["jesuschrist", "authority", "earth", "remission", "sins"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FORGIVE_SINS",
    en_title: "Quote: FORGIVE SINS",
    en_content: "Only GOD The Word (in the Person of The Lord Jesus Christ) has authority on Earth to forgive sins and apply His own Blood to the soul of the sinner!"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FORGIVE_SINS"})
MATCH (c:CONTENT {name: "content.FORGIVE_SINS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FORGIVE_SINS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.MERCY"})
MATCH (child:QUOTE {name: "quote.FORGIVE_SINS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.MERCY->FORGIVE_SINS"}]->(child);

```
