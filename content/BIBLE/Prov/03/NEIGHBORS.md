---
name: passage.NEIGHBORS
alias: "Passage: NEIGHBORS"
type: PASSAGE
parent: topic.SOCIOLOGY
tags:
- scheme
- neighbor
- innocent
- contention
- motive
neo4j: true
ptopic: "[[topic-SOCIOLOGY]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.NEIGHBORS",
    alias: "Passage: NEIGHBORS",
    parent: "topic.SOCIOLOGY",
    tags: ["scheme", "neighbor", "innocent", "contention", "motive"],
    source: "'Proverbs 3:29,30'",
    sortedsource: "'Proverbs 03:29-30'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs%203%3A29-30&version=ESV)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NEIGHBORS",
    en_title: "NEIGHBORS",
    en_content: "Do not plan evil against your neighbor,"
});

// LINK CONTENT
MATCH (b:PASSAGE), (c:CONTENT)
WHERE b.name = "passage.NEIGHBORS" AND c.name = "content.NEIGHBORS"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.NEIGHBORS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:PASSAGE)
WHERE parent.name = "topic.SOCIOLOGY" AND child.name = "passage.NEIGHBORS"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.SOCIOLOGY->NEIGHBORS"}]->(child);

```
