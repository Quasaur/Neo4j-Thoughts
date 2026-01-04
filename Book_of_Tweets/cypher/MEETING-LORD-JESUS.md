---
name: "thought.MEETING LORD JESUS"
alias: "Thought: Meeting Lord Jesus"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- jesus
- commitment
- life
- death
- faith
level: 1
neo4j: true
insert: true
---
# Meeting Lord Jesus

> [!Thought-en]
> I have met the Lord Jesus: He is to live for, and to die for!

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.MEETING LORD JESUS",
    alias: "Thought: Meeting Lord Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'commitment', 'life', 'death', 'faith'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MEETING LORD JESUS",
    en_title: "Meeting Lord Jesus",
    en_content: "I have met the Lord Jesus: He is to live for, and to die for!",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MEETING LORD JESUS" AND c.name = "content.MEETING LORD JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEETING LORD JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MEETING LORD JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MEETING LORD JESUS" }]->(child);
```