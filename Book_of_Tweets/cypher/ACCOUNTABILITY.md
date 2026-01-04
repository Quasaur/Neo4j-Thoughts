---
name: "thought.ACCOUNTABILITY"
alias: "Thought: Accountability"
type: THOUGHT
en_content: "God doesn't spare you the consequences of my actions."
parent: "topic.MORALITY"
tags:
- accountability
- consequences
- morality
- responsibility
- justice
level: 3
neo4j: true
insert: true
---
# Accountability

> [!Thought-en]
> God doesn't spare you the consequences of my actions.

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: Accountability",
    parent: "topic.MORALITY",
    tags: ['accountability', 'consequences', 'morality', 'responsibility', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    en_title: "Accountability",
    en_content: "God doesn't spare you the consequences of my actions.",
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
WHERE t.name = "thought.ACCOUNTABILITY" AND c.name = "content.ACCOUNTABILITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ACCOUNTABILITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.ACCOUNTABILITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ACCOUNTABILITY" }]->(child);
```