---
name: quote.WHERE_IS_GOD?
alias: "Quote: Quote: WHERE IS GOD?"
type: QUOTE
parent: topic.DIVINE-SOVEREIGNTY
tags:
- unperceived
- spiritualdeath
- separation
- evil
- nofellowship
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WHERE_IS_GOD?",
    alias: "Quote: Quote: WHERE IS GOD?",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["unperceived", "spiritualdeath", "separation", "evil", "nofellowship"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WHERE_IS_GOD?",
    en_title: "Quote: WHERE IS GOD?",
    en_content: "GOD is the eight-billion-ton Leviathan in the room...yet you cannot see, hear, smell, taste, touch or perceive Him. Spiritists and other occult adepts with years of experience in the spirit realm seriously doubt His Existence because they've never encountered Him, though He fills all things ([Jeremiah 23:24](https://www.biblegateway.com/passage/?search=Jeremiah+23%3A24&version=ESV))...WHY is that? It is because they, like you and i, are EVIL and therefore enemies of GOD. And like you and i, they are DEAD to Him and His Transcendently HOLY Nature."
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.WHERE_IS_GOD?" AND c.name = "content.WHERE_IS_GOD?"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WHERE_IS_GOD?"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "quote.WHERE_IS_GOD?"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->WHERE_IS_GOD?"}]->(child);

```
