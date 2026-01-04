---
name: "thought.GOD CONFIDENCE"
alias: "Thought: God Confidence"
type: THOUGHT
parent: "topic.FAITH"
tags:
- faith
- confidence
- self
- god
- truth
level: 4
neo4j: true
insert: true
---
# God Confidence

> [!Thought-en]
> God-confidence is better than self-confidence.

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.GOD CONFIDENCE",
    alias: "Thought: God Confidence",
    parent: "topic.FAITH",
    tags: ['faith', 'confidence', 'self', 'god', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GOD CONFIDENCE",
    en_title: "God Confidence",
    en_content: "God-confidence is better than self-confidence.",
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
WHERE t.name = "thought.GOD CONFIDENCE" AND c.name = "content.GOD CONFIDENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD CONFIDENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.GOD CONFIDENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >GOD CONFIDENCE" }]->(child);
```