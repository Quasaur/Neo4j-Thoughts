---
name: passage.FREEDOM_OF_DEATH
alias: "Passage: FREEDOM OF DEATH"
type: PASSAGE
parent: topic.FREEDOM
tags:
- freedom
- death
- sin
- thecross
- jesuschrist
neo4j: true
ptopic: "[[topic-FREEDOM]]"
level: 5
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.FREEDOM_OF_DEATH",
    alias: "Passage: FREEDOM OF DEATH",
    parent: "topic.FREEDOM",
    tags: ["freedom", "death", "sin", "thecross", "jesuschrist"],
    source: "'Romans 6:7'",
    sortedsource: "'Romans 06:07'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Romans+6:7&version=KJV)",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FREEDOM_OF_DEATH",
    en_title: "FREEDOM OF DEATH",
    en_content: "For he that is dead is freed from sin."
});

// LINK CONTENT
MATCH (b:PASSAGE), (c:CONTENT)
WHERE b.name = "passage.FREEDOM_OF_DEATH" AND c.name = "content.FREEDOM_OF_DEATH"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.FREEDOM_OF_DEATH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:PASSAGE)
WHERE parent.name = "topic.FREEDOM" AND child.name = "passage.FREEDOM_OF_DEATH"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.FREEDOM->FREEDOM_OF_DEATH"}]->(child);

```
