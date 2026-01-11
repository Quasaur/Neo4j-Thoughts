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
    es_title: "Toda Verdad es de Dios",
    es_content: "Toda verdad pertenece a Dios.",
    fr_title: "Toute Vérité Appartient à Dieu",
    fr_content: "Toute vérité appartient à Dieu.",
    hi_title: "सभी सत्य परमेश्वर के हैं",
    hi_content: "सभी सत्य परमेश्वर के हैं।",
    zh_title: "一切真理属于神",
    zh_content: "一切真理都属于神。"
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
