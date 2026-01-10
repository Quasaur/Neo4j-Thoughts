---
name: "thought.DNA MEMORY VS REINCARNATION"
alias: "Thought: Dna Memory Vs Reincarnation"
type: THOUGHT
en_content: "Reincarnation: what if these memories are not of previous lives, but of the lives of our ancestors engraved on our spirits/DNA?"
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- reincarnation
- dna
- memory
- biology
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.DNA MEMORY VS REINCARNATION",
    alias: "Thought: Dna Memory Vs Reincarnation",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'reincarnation', 'dna', 'memory', 'biology'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DNA MEMORY VS REINCARNATION",
    en_title: "Dna Memory Vs Reincarnation",
    en_content: "Reincarnation: what if these memories are not of previous lives, but of the lives of our ancestors engraved on our spirits/DNA?",
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
WHERE t.name = "thought.DNA MEMORY VS REINCARNATION" AND c.name = "content.DNA MEMORY VS REINCARNATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DNA MEMORY VS REINCARNATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DNA MEMORY VS REINCARNATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DNA MEMORY VS REINCARNATION" }]->(child);
```
