---
name: passage.PRIDE-AS-EVIL
alias: "Passage: PRIDE-AS-EVIL"
type: PASSAGE
parent: topic.HUMILITY
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
    name: "passage.PRIDE-AS-EVIL",
    alias: "Passage: PRIDE-AS-EVIL",
    parent: "topic.HUMILITY",
    tags: ["trust", "faith", "selfdoubt", "acknowledge", "promise"],
    source: "'Proverbs 3:7,8'",
    sortedsource: "'Proverbs 03:07,09'",
    biblelink: "(https://www.biblegateway.com/passage/?search=Proverbs+3%3A7-8&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PRIDE-AS-EVIL",
    en_title: "PRIDE-AS-EVIL",
    en_content: "Do not be wise in your own eyes; Fear the LORD and turn away from evil. It will be healing to your body And refreshment to your bones."
});

// LINK CONTENT
MATCH (b:PASSAGE), (c:CONTENT)
WHERE b.name = "passage.PRIDE-AS-EVIL" AND c.name = "content.PRIDE-AS-EVIL"
MERGE (b)-[:HAS_CONTENT {name: "b.edge.PRIDE-AS-EVIL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC), (child:PASSAGE)
WHERE parent.name = "topic.HUMILITY" AND child.name = "passage.PRIDE-AS-EVIL"
MERGE (parent)-[:HAS_PASSAGE {name: "b.edge.HUMILITY->PRIDE-AS-EVIL"}]->(child);

```
