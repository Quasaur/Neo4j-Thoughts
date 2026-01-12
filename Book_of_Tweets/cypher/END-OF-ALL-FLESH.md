---
name: "thought.END OF ALL FLESH"
alias: "Thought: End Of All Flesh"
type: THOUGHT
en_content: "\"The end of all flesh is come before Me...\" -- God"
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- sovereignty
- end_times
- justice
- divinity
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.END OF ALL FLESH",
    alias: "Thought: End Of All Flesh",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'sovereignty', 'end_times', 'justice', 'divinity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.END OF ALL FLESH",
    en_title: "End Of All Flesh",
    en_content: "\"The end of all flesh is come before Me...\" -- God",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.END OF ALL FLESH" AND c.name = "content.END OF ALL FLESH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.END OF ALL FLESH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.END OF ALL FLESH"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >END OF ALL FLESH" }]->(child);
```
