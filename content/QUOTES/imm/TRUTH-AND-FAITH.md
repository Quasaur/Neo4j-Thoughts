---
name: quote.TRUTH_AND_FAITH
alias: "Quote: Quote: TRUTH AND FAITH"
type: QUOTE
parent: topic.THE-GOSPEL
tags:
- faith
- truth
- salvation
- lakeoffire
- love
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.TRUTH_AND_FAITH",
    alias: "Quote: Quote: TRUTH AND FAITH",
    parent: "topic.THE-GOSPEL",
    tags: ["faith", "truth", "salvation", "lakeoffire", "love"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRUTH_AND_FAITH",
    en_title: "Quote: TRUTH AND FAITH",
    en_content: "GOD lovingly provides both the Truth that saves us from the Lake of Fire as well as the Saving Faith necessary to believe on (from the heart) and live by that Saving Truth."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.TRUTH_AND_FAITH" AND c.name = "content.TRUTH_AND_FAITH"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.TRUTH_AND_FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "quote.TRUTH_AND_FAITH"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->TRUTH_AND_FAITH"}]->(child);

```
