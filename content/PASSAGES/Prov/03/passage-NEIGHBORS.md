---
type: PASSAGE
name: "passage.NEIGHBORS"
alias: "Passage: Neighbors"
parent: "topic.SOCIOLOGY"
en_content: "Do not plan evil against your neighbor,"
tags: ["scheme", "neighbor", "innocent", "contention", "motive"]
ptopic: "[[topic-SOCIOLOGY]]"
level: 4
neo4j: true
---

```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.NEIGHBORS",
    alias: "Passage: Neighbors",
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
    ctype: "PASSAGE",
    en_title: "Neighbors",
    en_content: "Do not plan evil against your neighbor,",
 es_title: "VECINOS",
 es_content: "No planees el mal contra tu prójimo,",
 fr_title: "VOISINS",
 fr_content: "Ne planifie pas de mal contre ton prochain,",
 hi_title: "पड़ोसी",
 hi_content: "अपने पड़ोसी के विरुद्ध बुरी योजना न बनाओ,",
 zh_title: "lín jū",
 zh_content: "bù kě móu hài lín shè ，",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.NEIGHBORS"})
MATCH (c:CONTENT {name: "content.NEIGHBORS"})
MERGE (b)-[:HAS_CONTENT {name: "p.edge.NEIGHBORS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.SOCIOLOGY"})
MATCH (child:PASSAGE {name: "passage.NEIGHBORS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.SOCIOLOGY->NEIGHBORS"}]->(child);

```
