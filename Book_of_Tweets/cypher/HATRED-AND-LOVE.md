---
name: "thought.HATRED AND LOVE"
alias: "Thought: Hatred And Love"
type: THOUGHT
en_content: "One who is incapable of hatred is also incapable of love."
parent: "topic.PHILOSOPHY"
tags:
- love
- hatred
- character
- philosophy
- truth
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Nov-2012)
CREATE (t:THOUGHT {
    name: "thought.HATRED AND LOVE",
    alias: "Thought: Hatred And Love",
    parent: "topic.PHILOSOPHY",
    tags: ['love', 'hatred', 'character', 'philosophy', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HATRED AND LOVE",
    en_title: "Hatred And Love",
    en_content: "One who is incapable of hatred is also incapable of love.",
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
WHERE t.name = "thought.HATRED AND LOVE" AND c.name = "content.HATRED AND LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HATRED AND LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.HATRED AND LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >HATRED AND LOVE" }]->(child);
```
