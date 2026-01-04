---
name: quote.WEALTH_AND_FAITH
alias: "Quote: Quote: WEALTH AND FAITH"
type: QUOTE
parent: topic.WEALTH
tags:
- wealth
- faith
- exclusivity
- sovereignty
- heaven
neo4j: true
level: 3
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WEALTH_AND_FAITH",
    alias: "Quote: Quote: WEALTH AND FAITH",
    parent: "topic.WEALTH",
    tags: ["wealth", "faith", "exclusivity", "sovereignty", "heaven"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WEALTH_AND_FAITH",
    en_title: "Quote: WEALTH AND FAITH",
    en_content: "Wealth and Faith are mutually exclusive: having one, it does not necessarily follow that you will have the other in this life. When it comes to His Own, GOD determines the economic station of His Children. In perspective, however, there are no poor people in Heaven: you may have to wait till Eternity to receive your wealth (Matthew 6:19,20)."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.WEALTH_AND_FAITH" AND c.name = "content.WEALTH_AND_FAITH"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WEALTH_AND_FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.WEALTH" AND child.name = "quote.WEALTH_AND_FAITH"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WEALTH->WEALTH_AND_FAITH"}]->(child);

```
