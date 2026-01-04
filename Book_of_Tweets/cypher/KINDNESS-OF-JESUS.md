---
name: "thought.KINDNESS OF JESUS"
alias: "Thought: Kindness Of Jesus"
type: THOUGHT
en_content: "I have NEVER met anyone more kind that Jesus...and I never will!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- kindness
- love
- divinity
- compassion
level: 1
neo4j: true
insert: true
---
# Kindness Of Jesus

> [!Thought-en]
> I have NEVER met anyone more kind that Jesus...and I never will!

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2010b)
CREATE (t:THOUGHT {
    name: "thought.KINDNESS OF JESUS",
    alias: "Thought: Kindness Of Jesus",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'kindness', 'love', 'divinity', 'compassion'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.KINDNESS OF JESUS",
    en_title: "Kindness Of Jesus",
    en_content: "I have NEVER met anyone more kind that Jesus...and I never will!",
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
WHERE t.name = "thought.KINDNESS OF JESUS" AND c.name = "content.KINDNESS OF JESUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.KINDNESS OF JESUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.KINDNESS OF JESUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >KINDNESS OF JESUS" }]->(child);
```