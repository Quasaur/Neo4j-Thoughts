---
type: PASSAGE
name: "passage.REMOVING ALL THINGS"
alias: "Passage: Removing All Things"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "\"
 es_title: "Eliminando todas las cosas"
 es_content: ""
 fr_title: "Supprimer toutes choses"
 fr_content: ""
 hi_title: "सभी चीज़ें हटाना"
 hi_content: ""
 zh_title: "shān chú suǒ yǒu dōng xī"
 zh_content: ""
tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.REMOVING ALL THINGS",
    alias: "Passage: Removing All Things",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"],
    source: "",
    sortedsource: "",
    biblelink: "()",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.REMOVING",
    ctype: "PASSAGE",
    en_title: "Removing All Things",
    en_content: "\",
 es_title: "Eliminando todas las cosas",
 es_content: "",
 fr_title: "Supprimer toutes choses",
 fr_content: "",
 hi_title: "सभी चीज़ें हटाना",
 hi_content: "",
 zh_title: "shān chú suǒ yǒu dōng xī",
 zh_content: ""
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.REMOVING ALL THINGS"})
MATCH (c:CONTENT {name: "content.REMOVING"})
MERGE (b)-[:HAS_CONTENT {name: "p.edge.REMOVING ALL THINGS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:PASSAGE {name: "passage.REMOVING ALL THINGS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.DIVINE SOVEREIGNTY->REMOVING ALL THINGS"}]->(child);