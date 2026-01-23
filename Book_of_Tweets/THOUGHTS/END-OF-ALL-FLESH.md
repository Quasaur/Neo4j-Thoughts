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
neo4j: false
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
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
    es_title: "Fin de toda carne",
    es_content: "\",
    fr_title: "Fin de toute chair",
    fr_content: "\",
    hi_title: "सभी मांस का अंत",
    hi_content: "\",
    zh_title: "所有肉体的终结",
    zh_content: "\"
});

MATCH (t:THOUGHT {name: "thought.END OF ALL FLESH"})
MATCH (c:CONTENT {name: "content.END OF ALL FLESH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.END OF ALL FLESH" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.END OF ALL FLESH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->END OF ALL FLESH" }]->(child);
```
