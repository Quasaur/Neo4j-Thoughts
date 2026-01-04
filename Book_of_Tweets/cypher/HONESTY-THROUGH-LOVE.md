---
name: "thought.HONESTY THROUGH LOVE"
alias: "Thought: Honesty Through Love"
type: THOUGHT
en_content: "When you know God loves you, it's easier to be honest about your faults."
parent: "topic.ATTITUDE"
tags:
- honesty
- love
- faults
- attitude
- character
level: 2
neo4j: true
insert: true
---
# Honesty Through Love

> [!Thought-en]
> When you know God loves you, it's easier to be honest about your faults.

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Jun-2012a)
CREATE (t:THOUGHT {
    name: "thought.HONESTY THROUGH LOVE",
    alias: "Thought: Honesty Through Love",
    parent: "topic.ATTITUDE",
    tags: ['honesty', 'love', 'faults', 'attitude', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HONESTY THROUGH LOVE",
    en_title: "Honesty Through Love",
    en_content: "When you know God loves you, it's easier to be honest about your faults.",
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
WHERE t.name = "thought.HONESTY THROUGH LOVE" AND c.name = "content.HONESTY THROUGH LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HONESTY THROUGH LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HONESTY THROUGH LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >HONESTY THROUGH LOVE" }]->(child);
```