---
name: quote.THE_MEANING_OF_LIFE
alias: "Quote: Quote: The MEANING OF LIFE"
type: QUOTE
parent: topic.PHILOSOPHY
tags:
- lakeoffire
- sulfur
- wrath
- torment
- breathless
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_MEANING_OF_LIFE",
    alias: "Quote: Quote: The MEANING OF LIFE",
    parent: "topic.PHILOSOPHY",
    tags: ["lakeoffire", "sulfur", "wrath", "torment", "breathless"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_MEANING_OF_LIFE",
    en_title: "Quote: The MEANING OF LIFE",
    en_content: "Most importantly you will finally meet your Creator; and the moment you gaze into His Piercing Eyes you will realize with relentless clarity that your existence was never about you but was all about Him. He is truly the Center of all attention, the Cause of all excitement, the Objective of all worship, the Fountain of all life, the Nexus of all reality and the Meaning behind all chaos. Even evil itself, as brief a part it played in the panorama of cosmic history, only existed to serve His marvelous Purpose...then to be no more forever."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_MEANING_OF_LIFE" AND c.name = "content.THE_MEANING_OF_LIFE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_MEANING_OF_LIFE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "quote.THE_MEANING_OF_LIFE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.PHILOSOPHY->THE_MEANING_OF_LIFE"}]->(child);

```
