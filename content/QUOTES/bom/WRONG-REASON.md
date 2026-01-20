---
name: quote.WRONG_REASON
alias: "Quote: Quote: WRONG REASON"
type: QUOTE
parent: topic.ATTITUDE
tags:
- deed
- reason
- attitude
- parable
- prayer
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WRONG_REASON",
    alias: "Quote: Quote: WRONG REASON",
    parent: "topic.ATTITUDE",
    tags: ["deed", "reason", "attitude", "parable", "prayer"],
    source: "'The Basics and More: A Year's Sermons'",
    booklink: "(https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WRONG_REASON",
    en_title: "Quote: WRONG REASON",
    en_content: "IT IS POSSIBLE TO PERFORM A GOOD DEED FOR THE WRONG REASON (Luke 18:9-14). Is there anything wrong with fasting or tithing? No; BUT the Pharisee's bad ATTITUDE turned his good deeds into iniquity!"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.WRONG_REASON"})
MATCH (c:CONTENT {name: "content.WRONG_REASON"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WRONG_REASON"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MATCH (child:QUOTE {name: "quote.WRONG_REASON"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->WRONG_REASON"}]->(child);

```
