---
name: "thought.NATURE OF THE GODHEAD"
alias: "Thought: Nature Of The Godhead"
type: THOUGHT
en_content: "Anyone who thinks they understand the Nature of the Godhead is a liar."
parent: "topic.THE GODHEAD"
tags:
- godhead
- mystery
- truth
- knowledge
- divinity
level: 1
neo4j: true
insert: true
---
# Nature Of The Godhead

> [!Thought-en]
> Anyone who thinks they understand the Nature of the Godhead is a liar.

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NATURE OF THE GODHEAD",
    alias: "Thought: Nature Of The Godhead",
    parent: "topic.THE GODHEAD",
    tags: ['godhead', 'mystery', 'truth', 'knowledge', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NATURE OF THE GODHEAD",
    en_title: "Nature Of The Godhead",
    en_content: "Anyone who thinks they understand the Nature of the Godhead is a liar.",
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
WHERE t.name = "thought.NATURE OF THE GODHEAD" AND c.name = "content.NATURE OF THE GODHEAD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATURE OF THE GODHEAD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NATURE OF THE GODHEAD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NATURE OF THE GODHEAD" }]->(child);
```