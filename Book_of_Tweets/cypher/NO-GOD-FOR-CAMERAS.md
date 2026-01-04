---
name: "thought.NO GOD FOR CAMERAS"
alias: "Thought: No God For Cameras"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- god
- performance
- cameras
- truth
- character
level: 1
neo4j: true
insert: true
---
# No God For Cameras

> [!Thought-en]
> I am convinced that God doesn't perform for cameras.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.NO GOD FOR CAMERAS",
    alias: "Thought: No God For Cameras",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'performance', 'cameras', 'truth', 'character'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NO GOD FOR CAMERAS",
    en_title: "No God For Cameras",
    en_content: "I am convinced that God doesn't perform for cameras.",
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
WHERE t.name = "thought.NO GOD FOR CAMERAS" AND c.name = "content.NO GOD FOR CAMERAS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO GOD FOR CAMERAS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NO GOD FOR CAMERAS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NO GOD FOR CAMERAS" }]->(child);
```