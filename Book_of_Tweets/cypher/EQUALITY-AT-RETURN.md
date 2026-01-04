---
name: "thought.EQUALITY AT RETURN"
alias: "Thought: Equality At Return"
type: THOUGHT
en_content: "True economic political and social equality will never exist on Earth until Christ returns."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- equality
- christ
- return
- politics
- society
level: 2
neo4j: true
insert: true
---
# Equality At Return

> [!Thought-en]
> True economic political and social equality will never exist on Earth until Christ returns.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012f)
CREATE (t:THOUGHT {
    name: "thought.EQUALITY AT RETURN",
    alias: "Thought: Equality At Return",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['equality', 'christ', 'return', 'politics', 'society'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EQUALITY AT RETURN",
    en_title: "Equality At Return",
    en_content: "True economic political and social equality will never exist on Earth until Christ returns.",
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
WHERE t.name = "thought.EQUALITY AT RETURN" AND c.name = "content.EQUALITY AT RETURN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EQUALITY AT RETURN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.EQUALITY AT RETURN"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >EQUALITY AT RETURN" }]->(child);
```