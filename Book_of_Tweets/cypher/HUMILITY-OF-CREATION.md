---
name: "thought.HUMILITY OF CREATION"
alias: "Thought: Humility Of Creation"
type: THOUGHT
en_content: "It was The Supreme Act of Humility for God, Who doesn't need anything, to create something!"
parent: "topic.THE GODHEAD"
tags:
- humility
- creation
- god
- majesty
- necessity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.HUMILITY OF CREATION",
    alias: "Thought: Humility Of Creation",
    parent: "topic.THE GODHEAD",
    tags: ['humility', 'creation', 'god', 'majesty', 'necessity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.HUMILITY OF CREATION",
    en_title: "Humility Of Creation",
    en_content: "It was The Supreme Act of Humility for God, Who doesn't need anything, to create something!",
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
WHERE t.name = "thought.HUMILITY OF CREATION" AND c.name = "content.HUMILITY OF CREATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMILITY OF CREATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.HUMILITY OF CREATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >HUMILITY OF CREATION" }]->(child);
```
