---
name: "thought.REMOVING ALL THINGS"
alias: "Thought: Removing All Things"
type: THOUGHT
en_content: "\"I will completely remove all things from the face of the earth,\" -- God, Zephaniah 1:2"
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- sovereignty
- bible
- earth
- prophecy
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011c)
CREATE (t:THOUGHT {
    name: "thought.REMOVING ALL THINGS",
    alias: "Thought: Removing All Things",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'sovereignty', 'bible', 'earth', 'prophecy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REMOVING ALL THINGS",
    en_title: "Removing All Things",
    en_content: "\"I will completely remove all things from the face of the earth,\" -- God, Zephaniah 1:2",
    es_title: "Eliminando todas las cosas",
    es_content: "\",
    fr_title: "Supprimer toutes choses",
    fr_content: "\",
    hi_title: "सभी चीज़ें हटाना",
    hi_content: "\",
    zh_title: "删除所有东西",
    zh_content: "\"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REMOVING ALL THINGS" AND c.name = "content.REMOVING ALL THINGS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REMOVING ALL THINGS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.REMOVING ALL THINGS"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >REMOVING ALL THINGS" }]->(child);
```
