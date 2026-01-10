---
name: quote.THE_HEART_OF_MANKIND
alias: "Quote: Quote: The HEART OF MANKIND"
type: QUOTE
parent: topic.RELIGION
ptopic: "[[topic-RELIGION]]"
tags:
- heart
- human
- ungodly
- jesuschrist
- propitiation
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_HEART_OF_MANKIND",
    alias: "Quote: Quote: The HEART OF MANKIND",
    parent: "topic.RELIGION",
    tags: ["heart", "human", "ungodly", "jesuschrist", "propitiation"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_HEART_OF_MANKIND",
    en_title: "Quote: The HEART OF MANKIND",
    en_content: "None of our achievements, advances, contributions, virtuous deeds or good intentions make up for our evil hearts (hearts that believe GOD is not necessary to live a fulfilling life) ...else Christ would not have had to present Himself as a Sacrifice in our stead."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.THE_HEART_OF_MANKIND" AND c.name = "content.THE_HEART_OF_MANKIND"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_HEART_OF_MANKIND"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.RELIGION" AND child.name = "quote.THE_HEART_OF_MANKIND"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->THE_HEART_OF_MANKIND"}]->(child);

```
