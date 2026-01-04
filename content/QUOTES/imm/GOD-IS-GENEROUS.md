---
name: quote.GOD_IS_GENEROUS
alias: "Quote: Quote: GOD IS GENEROUS"
type: QUOTE
parent: topic.GRACE
tags:
- god
- generous
- magnanimous
- gracious
- stingy
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.GOD_IS_GENEROUS",
    alias: "Quote: Quote: GOD IS GENEROUS",
    parent: "topic.GRACE",
    tags: ["god", "generous", "magnanimous", "gracious", "stingy"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.GOD_IS_GENEROUS",
    en_title: "Quote: GOD IS GENEROUS",
    en_content: "GOD IS GENEROUS! He is generous to angel and demon…saint and sinner. He is not only more generous than anyone else, He was generous before anyone else! Look at the size of your planet, your solar system, your galaxy, your local group of galaxies—your universe! Look at the size of your family, your clan, your tribe, your nation! For the Love of GOD…YOU EXIST!!! Forever dismiss from your mind the idea that GOD is stingy…YOU are stingy; GOD is immeasurably magnanimous!"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.GOD_IS_GENEROUS" AND c.name = "content.GOD_IS_GENEROUS"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GOD_IS_GENEROUS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.GRACE" AND child.name = "quote.GOD_IS_GENEROUS"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->GOD_IS_GENEROUS"}]->(child);

```
