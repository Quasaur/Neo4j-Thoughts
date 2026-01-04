---
name: quote.NO_OBLIGATION
alias: "Quote: Quote: NO OBLIGATION"
type: QUOTE
parent: topic.MERCY
tags:
- god
- sovereignty
- unowed
- leniency
- evil
neo4j: true
level: 5
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NO_OBLIGATION",
    alias: "Quote: Quote: NO OBLIGATION",
    parent: "topic.MERCY",
    tags: ["god", "sovereignty", "unowed", "leniency", "evil"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NO_OBLIGATION",
    en_title: "Quote: NO OBLIGATION",
    en_content: "GOD is under no obligation to be merciful to evil. Sinners are evil, and every human is a sinner. By the definitions of the terms “mercy” and “forgiveness,” these virtues can never be owed to the sinner. GOD would’ve been perfectly righteous and just to annihilate Adam and Eve before their offspring could permeate the surface of the Earth with the wretchedness and horror you see today. Even more so: GOD would’ve been just to shut Lucifer down before anyone else was affected."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.NO_OBLIGATION" AND c.name = "content.NO_OBLIGATION"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NO_OBLIGATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.MERCY" AND child.name = "quote.NO_OBLIGATION"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.MERCY->NO_OBLIGATION"}]->(child);

```
