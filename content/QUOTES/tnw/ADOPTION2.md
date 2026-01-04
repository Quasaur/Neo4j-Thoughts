---
name: quote.ADOPTION2
alias: "Quote: Quote: ADOPTION2"
type: QUOTE
parent: topic.GRACE
tags:
- bornagain
- rebirth
- holyspirit
- childofgod
- holyspirit
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ADOPTION2",
    alias: "Quote: Quote: ADOPTION2",
    parent: "topic.GRACE",
    tags: ["bornagain", "rebirth", "holyspirit", "childofgod", "holyspirit"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ADOPTION2",
    en_title: "Quote: ADOPTION2",
    en_content: "No doubt you can appreciate how important Conversion is to your Salvation. GOD does not exist to the world (or the religious) because, as unredeemed sinners, they do not have the Holy Spirit of GOD dwelling in them, as true Christians do."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.ADOPTION2" AND c.name = "content.ADOPTION2"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ADOPTION2"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.ADOPTION2"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->ADOPTION2"}]->(child);

```
