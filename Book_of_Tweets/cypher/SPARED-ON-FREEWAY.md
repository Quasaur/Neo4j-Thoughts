---
name: "thought.SPARED ON FREEWAY"
alias: "Thought: Spared On Freeway"
type: THOUGHT
en_content: "I lost my brakes on the freeway last nite; but God spared me from accident and injury and I got the car home."
parent: "topic.SPIRITUALITY"
tags:
- providence
- protection
- miracle
- gratitude
- safety
level: 2
neo4j: true
insert: true
---
# Spared On Freeway

> [!Thought-en]
> I lost my brakes on the freeway last nite; but God spared me from accident and injury and I got the car home.

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.SPARED ON FREEWAY",
    alias: "Thought: Spared On Freeway",
    parent: "topic.SPIRITUALITY",
    tags: ['providence', 'protection', 'miracle', 'gratitude', 'safety'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPARED ON FREEWAY",
    en_title: "Spared On Freeway",
    en_content: "I lost my brakes on the freeway last nite; but God spared me from accident and injury and I got the car home.",
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
WHERE t.name = "thought.SPARED ON FREEWAY" AND c.name = "content.SPARED ON FREEWAY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPARED ON FREEWAY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPARED ON FREEWAY"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SPARED ON FREEWAY" }]->(child);
```