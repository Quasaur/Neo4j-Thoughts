---
name: "thought.NOTHING TO WORLD"
alias: "Thought: Nothing To World"
type: THOUGHT
en_content: "You cannot be something in God until you are nothing to the world."
parent: "topic.SPIRITUALITY"
tags:
- spirituality
- surrender
- world
- identity
- humility
level: 2
neo4j: true
insert: true
---
# Nothing To World

> [!Thought-en]
> You cannot be something in God until you are nothing to the world.

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011a)
CREATE (t:THOUGHT {
    name: "thought.NOTHING TO WORLD",
    alias: "Thought: Nothing To World",
    parent: "topic.SPIRITUALITY",
    tags: ['spirituality', 'surrender', 'world', 'identity', 'humility'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOTHING TO WORLD",
    en_title: "Nothing To World",
    en_content: "You cannot be something in God until you are nothing to the world.",
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
WHERE t.name = "thought.NOTHING TO WORLD" AND c.name = "content.NOTHING TO WORLD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING TO WORLD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NOTHING TO WORLD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NOTHING TO WORLD" }]->(child);
```