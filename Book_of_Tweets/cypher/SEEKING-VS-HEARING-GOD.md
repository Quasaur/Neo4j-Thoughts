---
name: "thought.SEEKING VS HEARING GOD"
alias: "Thought: Seeking Vs Hearing God"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- seeking
- hearing
- god
- desperation
- spirituality
level: 2
neo4j: true
insert: true
---
# Seeking Vs Hearing God

> [!Thought-en]
> You would think that a person desperate to hear from God would be desperate to seek God...

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.SEEKING VS HEARING GOD",
    alias: "Thought: Seeking Vs Hearing God",
    parent: "topic.SPIRITUALITY",
    tags: ['seeking', 'hearing', 'god', 'desperation', 'spirituality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SEEKING VS HEARING GOD",
    en_title: "Seeking Vs Hearing God",
    en_content: "You would think that a person desperate to hear from God would be desperate to seek God...",
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
WHERE t.name = "thought.SEEKING VS HEARING GOD" AND c.name = "content.SEEKING VS HEARING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SEEKING VS HEARING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SEEKING VS HEARING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SEEKING VS HEARING GOD" }]->(child);
```