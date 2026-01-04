---
name: "thought.INTELLIGENT DESIGN PROOF"
alias: "Thought: Intelligent Design Proof"
type: THOUGHT
en_content: "There is TONS of evidence for Intelligent Design evolutionists don't want you to know."
parent: "topic.CREATION"
tags:
- creation
- design
- evolution
- evidence
- truth
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011g)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT DESIGN PROOF",
    alias: "Thought: Intelligent Design Proof",
    parent: "topic.CREATION",
    tags: ['creation', 'design', 'evolution', 'evidence', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT DESIGN PROOF",
    en_title: "Intelligent Design Proof",
    en_content: "There is TONS of evidence for Intelligent Design evolutionists don't want you to know.",
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
WHERE t.name = "thought.INTELLIGENT DESIGN PROOF" AND c.name = "content.INTELLIGENT DESIGN PROOF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTELLIGENT DESIGN PROOF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.INTELLIGENT DESIGN PROOF"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >INTELLIGENT DESIGN PROOF" }]->(child);
```
