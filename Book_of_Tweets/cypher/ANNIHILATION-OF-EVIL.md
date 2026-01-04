---
name: "thought.ANNIHILATION OF EVIL"
alias: "Thought: Annihilation Of Evil"
type: THOUGHT
en_content: "Evil itself is doomed to annihilation...forever."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- evil
- destruction
- sovereignty
- prophecy
- forever
level: 2
neo4j: true
insert: true
---
# Annihilation Of Evil

> [!Thought-en]
> Evil itself is doomed to annihilation...forever.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.ANNIHILATION OF EVIL",
    alias: "Thought: Annihilation Of Evil",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['evil', 'destruction', 'sovereignty', 'prophecy', 'forever'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ANNIHILATION OF EVIL",
    en_title: "Annihilation Of Evil",
    en_content: "Evil itself is doomed to annihilation...forever.",
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
WHERE t.name = "thought.ANNIHILATION OF EVIL" AND c.name = "content.ANNIHILATION OF EVIL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ANNIHILATION OF EVIL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.ANNIHILATION OF EVIL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >ANNIHILATION OF EVIL" }]->(child);
```