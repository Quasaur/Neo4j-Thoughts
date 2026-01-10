---
name: passage.NOT-OF-FAITH
alias: "Passage: NOT-OF-FAITH"
type: PASSAGE
parent: topic.FAITH
tags:
- faith
- doubt
- condemnation
- sin
- wordofgod
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.NOT-OF-FAITH",
    alias: "Passage: NOT-OF-FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "doubt", "condemnation", "sin", "wordofgod"],
    source: "'Romans 14:23'",
    sortedsource: "'Romans 14:23'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Romans+14%3A23&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NOT-OF-FAITH",
    en_title: "NOT-OF-FAITH",
    en_content: "But the one who doubts is condemned if he eats, because his eating is not from faith; and whatever is not from faith is sin."
});

// LINK CONTENT
MATCH (b:PASSAGE), (c:CONTENT)
WHERE b.name = "passage.NOT-OF-FAITH" AND c.name = "content.NOT-OF-FAITH"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.NOT-OF-FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:PASSAGE)
WHERE parent.name = "topic.FAITH" AND child.name = "passage.NOT-OF-FAITH"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.FAITH->NOT-OF-FAITH"}]->(child);

```
