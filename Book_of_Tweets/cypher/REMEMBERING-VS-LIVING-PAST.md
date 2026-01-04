---
name: "thought.REMEMBERING VS LIVING PAST"
alias: "Thought: Remembering Vs Living Past"
type: THOUGHT
en_content: "There's no sin in remembering the past...only in trying to live in it."
parent: "topic.ATTITUDE"
tags:
- past
- memory
- attitude
- sin
- character
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.REMEMBERING VS LIVING PAST",
    alias: "Thought: Remembering Vs Living Past",
    parent: "topic.ATTITUDE",
    tags: ['past', 'memory', 'attitude', 'sin', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REMEMBERING VS LIVING PAST",
    en_title: "Remembering Vs Living Past",
    en_content: "There's no sin in remembering the past...only in trying to live in it.",
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
WHERE t.name = "thought.REMEMBERING VS LIVING PAST" AND c.name = "content.REMEMBERING VS LIVING PAST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REMEMBERING VS LIVING PAST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.REMEMBERING VS LIVING PAST"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >REMEMBERING VS LIVING PAST" }]->(child);
```
