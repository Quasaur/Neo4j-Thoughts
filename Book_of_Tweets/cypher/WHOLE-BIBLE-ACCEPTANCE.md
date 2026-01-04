---
name: "thought.WHOLE BIBLE ACCEPTANCE"
alias: "Thought: Whole Bible Acceptance"
type: THOUGHT
en_content: "We should accept the whole Bible, or none of it; otherwise we distort its message."
parent: "topic.TRUTH"
tags:
- bible
- truth
- distortion
- message
- authority
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.WHOLE BIBLE ACCEPTANCE",
    alias: "Thought: Whole Bible Acceptance",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'distortion', 'message', 'authority'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WHOLE BIBLE ACCEPTANCE",
    en_title: "Whole Bible Acceptance",
    en_content: "We should accept the whole Bible, or none of it; otherwise we distort its message.",
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
WHERE t.name = "thought.WHOLE BIBLE ACCEPTANCE" AND c.name = "content.WHOLE BIBLE ACCEPTANCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WHOLE BIBLE ACCEPTANCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.WHOLE BIBLE ACCEPTANCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >WHOLE BIBLE ACCEPTANCE" }]->(child);
```
