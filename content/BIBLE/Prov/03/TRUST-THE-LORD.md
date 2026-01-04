---
name: passage.TRUST_THE_LORD
alias: "Passage: 'Passage: TRUST THE LORD'"
type: PASSAGE
parent: topic.FAITH
tags:
- trust
- faith
- selfdoubt
- acknowledge
- promise
neo4j: true
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.TRUST_THE_LORD",
    alias: "Passage: 'Passage: TRUST THE LORD'",
    parent: "topic.FAITH",
    tags: ["trust", "faith", "selfdoubt", "acknowledge", "promise"],
    source: "'Proverbs 3:5,6'",
    sortedsource: "'Proverbs 03:05-06'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A5-6&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRUST_THE_LORD",
    en_title: "'Passage: TRUST THE LORD'",
    en_content: "Trust in the LORD with all your heart And do not lean on your own understanding. In all your ways acknowledge Him, And He will make your paths straight."
});

// LINK CONTENT
MATCH (b:PASSAGE), (c:CONTENT)
WHERE b.name = "passage.TRUST_THE_LORD" AND c.name = "content.TRUST_THE_LORD"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.TRUST_THE_LORD"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:PASSAGE)
WHERE parent.name = "topic.FAITH" AND child.name = "passage.TRUST_THE_LORD"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.FAITH->TRUST_THE_LORD"}]->(child);

```
