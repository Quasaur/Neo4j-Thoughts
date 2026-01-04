---
name: "thought.TREASURE UNDER GARBAGE"
alias: "Thought: Treasure Under Garbage"
type: THOUGHT
en_content: "Treasure is often hidden under garbage...be a treasure hunter!"
parent: "topic.WISDOM"
tags:
- wisdom
- treasure
- perspective
- search
- character
level: 3
neo4j: true
insert: true
---
# Treasure Under Garbage

> [!Thought-en]
> Treasure is often hidden under garbage...be a treasure hunter!

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2012c)
CREATE (t:THOUGHT {
    name: "thought.TREASURE UNDER GARBAGE",
    alias: "Thought: Treasure Under Garbage",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'treasure', 'perspective', 'search', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TREASURE UNDER GARBAGE",
    en_title: "Treasure Under Garbage",
    en_content: "Treasure is often hidden under garbage...be a treasure hunter!",
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
WHERE t.name = "thought.TREASURE UNDER GARBAGE" AND c.name = "content.TREASURE UNDER GARBAGE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TREASURE UNDER GARBAGE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.TREASURE UNDER GARBAGE"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >TREASURE UNDER GARBAGE" }]->(child);
```