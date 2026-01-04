---
name: "thought.FLESH THE TYRANT"
alias: "Thought: Flesh The Tyrant"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- flesh
- tyrant
- sin
- humanity
- character
level: 3
neo4j: true
insert: true
---
# Flesh The Tyrant

> [!Thought-en]
> The Flesh is a tyrant.

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.FLESH THE TYRANT",
    alias: "Thought: Flesh The Tyrant",
    parent: "topic.HUMANITY",
    tags: ['flesh', 'tyrant', 'sin', 'humanity', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FLESH THE TYRANT",
    en_title: "Flesh The Tyrant",
    en_content: "The Flesh is a tyrant.",
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
WHERE t.name = "thought.FLESH THE TYRANT" AND c.name = "content.FLESH THE TYRANT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FLESH THE TYRANT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.FLESH THE TYRANT"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >FLESH THE TYRANT" }]->(child);
```