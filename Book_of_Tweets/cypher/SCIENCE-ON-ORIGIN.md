---
name: "thought.SCIENCE ON ORIGIN"
alias: "Thought: Science On Origin"
type: THOUGHT
en_content: "If I can't trust science to explain origin, why is it so infallible on development??"
parent: "topic.TRUTH"
tags:
- science
- origin
- development
- truth
- evolution
level: 2
neo4j: true
insert: true
---
# Science On Origin

> [!Thought-en]
> If I can't trust science to explain origin, why is it so infallible on development??

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011e)
CREATE (t:THOUGHT {
    name: "thought.SCIENCE ON ORIGIN",
    alias: "Thought: Science On Origin",
    parent: "topic.TRUTH",
    tags: ['science', 'origin', 'development', 'truth', 'evolution'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SCIENCE ON ORIGIN",
    en_title: "Science On Origin",
    en_content: "If I can't trust science to explain origin, why is it so infallible on development??",
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
WHERE t.name = "thought.SCIENCE ON ORIGIN" AND c.name = "content.SCIENCE ON ORIGIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SCIENCE ON ORIGIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SCIENCE ON ORIGIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SCIENCE ON ORIGIN" }]->(child);
```