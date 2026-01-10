---
name: "thought.ALL TRUTH GODS"
alias: "Thought: All Truth Gods"
type: THOUGHT
en_content: "All truth belongs to God."
parent: "topic.TRUTH"
tags:
- truth
- ownership
- god
- revelation
- philosophy
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Feb-2013)
CREATE (t:THOUGHT {
    name: "thought.ALL TRUTH GODS",
    alias: "Thought: All Truth Gods",
    parent: "topic.TRUTH",
    tags: ['truth', 'ownership', 'god', 'revelation', 'philosophy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ALL TRUTH GODS",
    en_title: "All Truth Gods",
    en_content: "All truth belongs to God.",
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
WHERE t.name = "thought.ALL TRUTH GODS" AND c.name = "content.ALL TRUTH GODS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALL TRUTH GODS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.ALL TRUTH GODS"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >ALL TRUTH GODS" }]->(child);
```
