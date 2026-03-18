---
type: THOUGHT
name: "thought.GOD LOVING EVERY SOUL"
alias: "Thought: God Loving Every Soul"
parent: "topic.THE GODHEAD"
en_content: "There is no soul created by God that He did not love."
tags: ["love", "soul", "creation", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Jul-2012)
CREATE (t:THOUGHT {    name: "thought.GOD LOVING EVERY SOUL",
    alias: "Thought: God Loving Every Soul",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'soul', 'creation', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.GOD LOVING EVERY SOUL",
    ctype: "THOUGHT",
    en_title: "God Loving Every Soul",
    en_content: "There is no soul created by God that He did not love.",
    es_title: "Dios Amando Cada Alma",
    es_content: "No hay alma creada por Dios que Él no haya amado.",
    fr_title: "Dieu Aimant Chaque Âme",
    fr_content: "Il n'y a aucune âme créée par Dieu qu'Il n'ait pas aimée.",
    hi_title: "परमेश्वर प्रत्येक आत्मा से प्रेम करता है",
    hi_content: "परमेश्वर द्वारा सृजित कोई भी आत्मा ऐसी नहीं है जिससे उसने प्रेम न किया हो।",
    zh_title: "Shàngdì Ài Měi Gè Línghún",
    zh_content: "Méiyǒu yī gè Shàngdì chuàngzào de línghún shì Tā bù ài de."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GOD LOVING EVERY SOUL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->GOD LOVING EVERY SOUL"
RETURN t, parent;
```
