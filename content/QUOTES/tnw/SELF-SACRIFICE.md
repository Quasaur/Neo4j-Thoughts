---
name: quote.SELF-SACRIFICE
alias: "Quote: Quote: SELF-SACRIFICE"
type: QUOTE
parent: topic.HUMILITY
tags:
- selfsacrifice
- submission
- offering
- love
- christfirst
neo4j: true
ptopic: "[[topic-HUMILITY]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.SELF-SACRIFICE",
    alias: "Quote: Quote: SELF-SACRIFICE",
    parent: "topic.HUMILITY",
    tags: ["selfsacrifice", "submission", "offering", "love", "christfirst"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.SELF-SACRIFICE",
    en_title: "Quote: SELF-SACRIFICE",
    en_content: "Did i drift off topic, Dear Reader? Not at all; the spirit of worship, obedience and self-sacrifice for the Glory of GOD is the product of True, Divinely-given Faith that exists in the heart, and not just the mind. GOD gave up That which was EVERYTHING to Him to love you; and if you truly desire to be filled with His Holy Spirit, That Selfsame Member of the Eternal GODHEAD will inspire you to the same level of self-sacrificial love we see in Christ Himself."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.SELF-SACRIFICE" AND c.name = "content.SELF-SACRIFICE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.SELF-SACRIFICE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.HUMILITY" AND child.name = "quote.SELF-SACRIFICE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMILITY->SELF-SACRIFICE"}]->(child);

```
