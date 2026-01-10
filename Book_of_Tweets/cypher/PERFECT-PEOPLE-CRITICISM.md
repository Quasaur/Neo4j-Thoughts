---
name: "thought.PERFECT PEOPLE CRITICISM"
alias: "Thought: Perfect People Criticism"
type: THOUGHT
en_content: "Have you ever noticed that perfect people don't respond well to criticism?"
parent: "topic.ATTITUDE"
tags:
- perfection
- criticism
- response
- attitude
- character
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.PERFECT PEOPLE CRITICISM",
    alias: "Thought: Perfect People Criticism",
    parent: "topic.ATTITUDE",
    tags: ['perfection', 'criticism', 'response', 'attitude', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PERFECT PEOPLE CRITICISM",
    en_title: "Perfect People Criticism",
    en_content: "Have you ever noticed that perfect people don't respond well to criticism?",
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
WHERE t.name = "thought.PERFECT PEOPLE CRITICISM" AND c.name = "content.PERFECT PEOPLE CRITICISM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PERFECT PEOPLE CRITICISM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.PERFECT PEOPLE CRITICISM"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >PERFECT PEOPLE CRITICISM" }]->(child);
```
