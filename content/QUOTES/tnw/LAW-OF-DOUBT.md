---
name: quote.LAW_OF_DOUBT
alias: "Quote: Quote: LAW OF DOUBT"
type: QUOTE
parent: topic.RELIGION
tags:
- doubt
- faiithless
- promise
- gospel
- fullassurance
neo4j: true
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.LAW_OF_DOUBT",
    alias: "Quote: Quote: LAW OF DOUBT",
    parent: "topic.RELIGION",
    tags: ["doubt", "faiithless", "promise", "gospel", "fullassurance"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.LAW_OF_DOUBT",
    en_title: "Quote: LAW OF DOUBT",
    en_content: "As stated in my book '[IMMUNITY to the Lake of Fire: a No-Nonsense Guide](https://www.clmbooks.life/book-ip)' religion has declared the doctrine of Full Assurance (Once Saved, Always Saved) to not only be a heresy, but an unforgivable sin (Council of Trent, Sixth Session, Chapter XVI, Canons on Justification). That is to say: Doubt itself, the sworn enemy of Faith ([Matthew 14:31](https://mobile.biblegateway.com/passage/?search=Matthew+14%3A31&version=ESV); [James 1:5-8](https://mobile.biblegateway.com/passage/?search=James+1%3A5-8&version=ESV)), is adopted by institutionalized religion as both critical and necessary. Gadzooks! What am i missing here? How can i walk with Jesus in full assurance of Faith if He can't even guarantee the completion of the Good Work our Heavenly Father began in me?"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.LAW_OF_DOUBT" AND c.name = "content.LAW_OF_DOUBT"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.LAW_OF_DOUBT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.RELIGION" AND child.name = "quote.LAW_OF_DOUBT"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->LAW_OF_DOUBT"}]->(child);

```
