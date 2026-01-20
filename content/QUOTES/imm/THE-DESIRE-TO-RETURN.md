---
name: quote.THE_DESIRE_TO_RETURN
alias: "Quote: Quote: THE DESIRE TO RETURN"
type: QUOTE
parent: topic.EVIL
tags:
- survival
- lakeoffire
- repentance
- sinner
- god
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_DESIRE_TO_RETURN",
    alias: "Quote: Quote: THE DESIRE TO RETURN",
    parent: "topic.EVIL",
    tags: ["survival", "lakeoffire", "repentance", "sinner", "god"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_DESIRE_TO_RETURN",
    en_title: "Quote: THE DESIRE TO RETURN",
    en_content: "While any sinner would DO EVERYTHING POSSIBLE to avoid the Lake of Fire, no sinner has ANY DESIRE IN THEIR HEART WHATSOEVER to return to God (repentance)."
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_DESIRE_TO_RETURN"})
MATCH (c:CONTENT {name: "content.THE_DESIRE_TO_RETURN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_DESIRE_TO_RETURN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.THE_DESIRE_TO_RETURN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->THE_DESIRE_TO_RETURN"}]->(child);

```
