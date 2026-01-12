---
name: "thought.DARK MATTER NEED"
alias: "Thought: Dark Matter Need"
type: THOUGHT
en_content: "If the Standard Model was doing its job, there'd be no need for \"dark matter\", \"dark energy\" or \"dark flow\"!"
parent: "topic.PHILOSOPHY"
tags:
- science
- dark_matter
- philosophy
- energy
- truth
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.DARK MATTER NEED",
    alias: "Thought: Dark Matter Need",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'dark_matter', 'philosophy', 'energy', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DARK MATTER NEED",
    en_title: "Dark Matter Need",
    en_content: "If the Standard Model was doing its job, there'd be no need for \"dark matter\", \"dark energy\" or \"dark flow\"!",
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
WHERE t.name = "thought.DARK MATTER NEED" AND c.name = "content.DARK MATTER NEED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DARK MATTER NEED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DARK MATTER NEED"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DARK MATTER NEED" }]->(child);
```
