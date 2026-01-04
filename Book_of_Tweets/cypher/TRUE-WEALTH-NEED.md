---
name: "thought.TRUE WEALTH NEED"
alias: "Thought: True Wealth Need"
type: THOUGHT
en_content: "Matthew 10:34-39: One is not truly wealthy until they've lost their need for everything!"
parent: "topic.PHILOSOPHY"
tags:
- wealth
- need
- philosophy
- character
- independence
level: 4
neo4j: true
insert: true
---
# True Wealth Need

> [!Thought-en]
> Matthew 10:34-39: One is not truly wealthy until they've lost their need for everything!

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.TRUE WEALTH NEED",
    alias: "Thought: True Wealth Need",
    parent: "topic.PHILOSOPHY",
    tags: ['wealth', 'need', 'philosophy', 'character', 'independence'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRUE WEALTH NEED",
    en_title: "True Wealth Need",
    en_content: "Matthew 10:34-39: One is not truly wealthy until they've lost their need for everything!",
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
WHERE t.name = "thought.TRUE WEALTH NEED" AND c.name = "content.TRUE WEALTH NEED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUE WEALTH NEED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.TRUE WEALTH NEED"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >TRUE WEALTH NEED" }]->(child);
```