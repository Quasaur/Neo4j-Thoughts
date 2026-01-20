---
name: quote.HEADING_HOME
alias: "Quote: Quote: HEADING HOME"
type: QUOTE
parent: topic.TRUTH
tags:
- home
- safety
- joy
- rest
- godhead
neo4j: true
ptopic: "[[topic-TRUTH]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HEADING_HOME",
    alias: "Quote: Quote: HEADING HOME",
    parent: "topic.TRUTH",
    tags: ["home", "safety", "joy", "rest", "godhead"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HEADING_HOME",
    en_title: "Quote: HEADING HOME",
    en_content: "Most people focus on the 'deny himself' clause, yet that is NOT the central idea of this statement. To be a disciple of Jesus you must FOLLOW Jesus...but WHERE IS JESUS GOING? In connection to what i said in [Part Fourteen](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) regarding Reality, Jesus is RETURNING TO THE FATHER where sin, death and affliction do not exist...and HE IS INVITING YOU TO RETURN THERE WITH HIM!!! This is the HEART of what being 'saved' means, with the added benefit of NEVER BEING CAPABLE OF SINNING AGAIN!!!!"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HEADING_HOME"})
MATCH (c:CONTENT {name: "content.HEADING_HOME"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HEADING_HOME"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:QUOTE {name: "quote.HEADING_HOME"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.TRUTH->HEADING_HOME"}]->(child);

```
