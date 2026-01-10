---
name: quote.FEELINGS
alias: "Quote: Quote: FEELINGS"
type: QUOTE
parent: topic.FAITH
tags:
- feelings
- emotions
- faith
- wordofgod
- believe
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FEELINGS",
    alias: "Quote: Quote: FEELINGS",
    parent: "topic.FAITH",
    tags: ["feelings", "emotions", "faith", "wordofgod", "believe"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FEELINGS",
    en_title: "Quote: FEELINGS",
    en_content: "Your personal neuroses (guilt, shame, depression, bipolar disorder, etc.) notwithstanding, when you pray GOD STOPS WHAT HE’S DOING AND LISTENS! Your perception of His Presence (or lack thereof) is irrelevant; what matters is the truth and your faith in the truth…not your feelings."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.FEELINGS" AND c.name = "content.FEELINGS"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FEELINGS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.FAITH" AND child.name = "quote.FEELINGS"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->FEELINGS"}]->(child);

```
