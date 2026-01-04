---
name: "thought.OWNING ALL THINGS"
alias: "Thought: Owning All Things"
type: THOUGHT
en_content: "Revelation 21:7: You cannot own ALL THINGS unless you no longer need them."
parent: "topic.PHILOSOPHY"
tags:
- ownership
- attachment
- philosophy
- desire
- abundance
level: 4
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.OWNING ALL THINGS",
    alias: "Thought: Owning All Things",
    parent: "topic.PHILOSOPHY",
    tags: ['ownership', 'attachment', 'philosophy', 'desire', 'abundance'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.OWNING ALL THINGS",
    en_title: "Owning All Things",
    en_content: "Revelation 21:7: You cannot own ALL THINGS unless you no longer need them.",
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
WHERE t.name = "thought.OWNING ALL THINGS" AND c.name = "content.OWNING ALL THINGS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OWNING ALL THINGS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.OWNING ALL THINGS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >OWNING ALL THINGS" }]->(child);
```
