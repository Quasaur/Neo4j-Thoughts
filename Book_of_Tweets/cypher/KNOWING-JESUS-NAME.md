---
name: "thought.KNOWING JESUS NAME"
alias: "Thought: Knowing Jesus Name"
type: THOUGHT
en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus."
parent: "topic.THE GODHEAD"
tags:
- jesus
- identity
- knowledge
- lord
- relationship
level: 1
neo4j: true
insert: true
---
# Knowing Jesus Name

> [!Thought-en]
> Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus.

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.KNOWING JESUS NAME",
    alias: "Thought: Knowing Jesus Name",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'knowledge', 'lord', 'relationship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.KNOWING JESUS NAME",
    en_title: "Knowing Jesus Name",
    en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.KNOWING JESUS NAME" AND c.name = "content.KNOWING JESUS NAME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.KNOWING JESUS NAME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.KNOWING JESUS NAME"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >KNOWING JESUS NAME" }]->(child);
```