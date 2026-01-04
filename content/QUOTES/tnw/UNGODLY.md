---
name: quote.UNGODLY
alias: "Quote: Quote: UNGODLY"
type: QUOTE
parent: topic.EVIL
tags:
- ungodly
- godless
- selfworship
- humanitarian
- damned
neo4j: true
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.UNGODLY",
    alias: "Quote: Quote: UNGODLY",
    parent: "topic.EVIL",
    tags: ["ungodly", "godless", "selfworship", "humanitarian", "damned"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.UNGODLY",
    en_title: "Quote: UNGODLY",
    en_content: "And this is what the Bible means by the term 'ungodly' ([Psalms 1:4,5](https://www.biblegateway.com/passage/?search=Psalms+1%3A4-5&version=ESV)): not that we deliberately choose to spend every waking moment committing atrocities, but that as much as we desire to live good, just and quiet lives, WE'D RATHER DO SO WITHOUT GOD."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.UNGODLY" AND c.name = "content.UNGODLY"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.UNGODLY"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.EVIL" AND child.name = "quote.UNGODLY"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->UNGODLY"}]->(child);

```
