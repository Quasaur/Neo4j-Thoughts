---
name: quote.THE_LAST_ADAM
alias: "Quote: Quote: THE LAST ADAM"
type: QUOTE
parent: topic.HUMANITY
tags:
- jesuschrist
- lastadam
- humanity
- exalted
- holyspirit
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_LAST_ADAM",
    alias: "Quote: Quote: THE LAST ADAM",
    parent: "topic.HUMANITY",
    tags: ["jesuschrist", "lastadam", "humanity", "exalted", "holyspirit"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_LAST_ADAM",
    en_title: "Quote: THE LAST ADAM",
    en_content: "Jesus is the most powerful human in the universe! And having in His Body exalted humanity beyond the reach of sin and affliction, He became the Last Adam of a new race of humanity, and has poured out His Divine Holy Spirit upon all who in faith call upon Him."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_LAST_ADAM"})
MATCH (c:CONTENT {name: "content.THE_LAST_ADAM"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_LAST_ADAM"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:QUOTE {name: "quote.THE_LAST_ADAM"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMANITY->THE_LAST_ADAM"}]->(child);

```
