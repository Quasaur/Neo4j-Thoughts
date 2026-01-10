---
name: quote.INCOMPATIBLE
alias: "Quote: Quote: INCOMPATIBLE"
type: QUOTE
parent: topic.SPIRITUALITY
tags:
- flesh
- spirit
- holyspirit
- god
- adoption
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.INCOMPATIBLE",
    alias: "Quote: Quote: INCOMPATIBLE",
    parent: "topic.SPIRITUALITY",
    tags: ["flesh", "spirit", "holyspirit", "god", "adoption"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.INCOMPATIBLE",
    en_title: "Quote: INCOMPATIBLE",
    en_content: "The life you were born into as a human is ABSOLUTELY INCOMPATIBLE with the Life you were born-again into as a Child of GOD."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.INCOMPATIBLE" AND c.name = "content.INCOMPATIBLE"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.INCOMPATIBLE"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "quote.INCOMPATIBLE"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.SPIRITUALITY->INCOMPATIBLE"}]->(child);

```
