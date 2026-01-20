---
name: quote.ETERNAL_DAMNATION
alias: "Quote: Quote: ETERNAL DAMNATION"
type: QUOTE
parent: topic.APOCALYPSE
tags:
- lakeoffire
- sulfur
- wrath
- torment
- breathless
neo4j: true
ptopic: "[[topic-APOCALYPSE]]"
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ETERNAL_DAMNATION",
    alias: "Quote: Quote: ETERNAL DAMNATION",
    parent: "topic.APOCALYPSE",
    tags: ["lakeoffire", "sulfur", "wrath", "torment", "breathless"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ETERNAL_DAMNATION",
    en_title: "Quote: ETERNAL DAMNATION",
    en_content: "Likewise, those who participate in the Second Resurrection will come forth completely intact: spirit, soul and body with no parts or organs missing. There is a reason the word 'resurrection' must be defined this way... Look carefully at the [Twentieth Chapter of Revelation](https://mobile.biblegateway.com/passage/?search=Revelation+20&version=KJV). After all of the Damned are resurrected Death and Hades (the place of disembodied souls) are themselves cast into the Lake of Fire and Sulfur! The implication is horrifyingly obvious: if Death no longer exists, then no matter what damage is done to you by the Fire and Sulfur, you can never die! There is no relief and there is no reprieve."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ETERNAL_DAMNATION"})
MATCH (c:CONTENT {name: "content.ETERNAL_DAMNATION"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ETERNAL_DAMNATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.APOCALYPSE"})
MATCH (child:QUOTE {name: "quote.ETERNAL_DAMNATION"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.APOCALYPSE->ETERNAL_DAMNATION"}]->(child);

```
