---
name: "thought.DISABILITY OF SPIRIT"
alias: "Thought: Disability Of Spirit"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- presence
- perception
- disability
- spirituality
- god
level: 2
neo4j: true
insert: true
---
# Disability Of Spirit

> [!Thought-en]
> The inability to perceive God's Immediate Presence is a greater disability than not being able to walk or see.

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.DISABILITY OF SPIRIT",
    alias: "Thought: Disability Of Spirit",
    parent: "topic.SPIRITUALITY",
    tags: ['presence', 'perception', 'disability', 'spirituality', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DISABILITY OF SPIRIT",
    en_title: "Disability Of Spirit",
    en_content: "The inability to perceive God's Immediate Presence is a greater disability than not being able to walk or see.",
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
WHERE t.name = "thought.DISABILITY OF SPIRIT" AND c.name = "content.DISABILITY OF SPIRIT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DISABILITY OF SPIRIT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.DISABILITY OF SPIRIT"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >DISABILITY OF SPIRIT" }]->(child);
```