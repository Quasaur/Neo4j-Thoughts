---
name: "thought.MOTHER OF JESUS"
alias: "Thought: Mother Of Jesus"
type: THOUGHT
en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God."
parent: "topic.THE GODHEAD"
tags:
- mary
- jesus
- divinity
- theology
- incarnation
level: 1
neo4j: true
insert: true
---
# Mother Of Jesus

> [!Thought-en]
> Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.MOTHER OF JESUS",
    alias: "Thought: Mother Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['mary', 'jesus', 'divinity', 'theology', 'incarnation'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MOTHER OF JESUS",
    en_title: "Mother Of Jesus",
    en_content: "Mary is the BIOLOGICAL mother of Jesus, not the SPIRITUAL mother of God.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MOTHER OF JESUS" AND c.name = "content.MOTHER OF JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOTHER OF JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MOTHER OF JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MOTHER OF JESUS" }]->(child);
```