---
name: "thought.DREAMS OTHER WORLDS"
alias: "Thought: Dreams Other Worlds"
type: THOUGHT
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- dreams
- existence
- universe
- imagination
level: 4
neo4j: true
insert: true
---
# Dreams Other Worlds

> [!Thought-en]
> What if dreams were peeks into another life...on another planet ...in another galaxy very similar to ours?

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.DREAMS OTHER WORLDS",
    alias: "Thought: Dreams Other Worlds",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'dreams', 'existence', 'universe', 'imagination'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DREAMS OTHER WORLDS",
    en_title: "Dreams Other Worlds",
    en_content: "What if dreams were peeks into another life...on another planet ...in another galaxy very similar to ours?",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DREAMS OTHER WORLDS" AND c.name = "content.DREAMS OTHER WORLDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DREAMS OTHER WORLDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DREAMS OTHER WORLDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DREAMS OTHER WORLDS" }]->(child);
```