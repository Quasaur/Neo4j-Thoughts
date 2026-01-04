---
name: quote.CHILD_OF_SATAN
alias: "Quote: Quote: CHILD OF SATAN"
type: QUOTE
parent: topic.EVIL
tags:
- evil
- wicked
- reprobate
- hopeless
- jesuschrist
neo4j: true
level: 4
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.CHILD_OF_SATAN",
    alias: "Quote: Quote: CHILD OF SATAN",
    parent: "topic.EVIL",
    tags: ["evil", "wicked", "reprobate", "hopeless", "jesuschrist"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.CHILD_OF_SATAN",
    en_title: "Quote: CHILD OF SATAN",
    en_content: "It is impossible to be a sinner and not harbor in your heart some lie that you cling to as truth. Do you even now yet see yourself as a 'good person' who could 'benefit' from having an 'advisor' such as Jesus at your side? Or are you willing to admit that you're a child of the Devil, by your very nature damned for Wrath and in DESPERATE NEED of the Only-Begotten Son of GOD's Mercy, Forgiveness and Saving Grace?"
});

// LINK CONTENT
MATCH (q:QUOTE), (c:CONTENT)
WHERE q.name = "quote.CHILD_OF_SATAN" AND c.name = "content.CHILD_OF_SATAN"
MERGE (q)-[:HAS_CONTENT {name: "q.edge.CHILD_OF_SATAN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:QUOTE)
WHERE parent.name = "topic.EVIL" AND child.name = "quote.CHILD_OF_SATAN"
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->CHILD_OF_SATAN"}]->(child);

```
