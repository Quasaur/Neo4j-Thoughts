---
name: "thought.KNOWLEDGE PROPERTY GOD"
alias: "Thought: Knowledge Property God"
type: THOUGHT
en_content: "Genesis 2:15, 16: Knowledge is not a right; knowledge is the property of God."
parent: "topic.TRUTH"
tags:
- knowledge
- ownership
- property
- god
- truth
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Mar-2013b)
CREATE (t:THOUGHT {
    name: "thought.KNOWLEDGE PROPERTY GOD",
    alias: "Thought: Knowledge Property God",
    parent: "topic.TRUTH",
    tags: ['knowledge', 'ownership', 'property', 'god', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.KNOWLEDGE PROPERTY GOD",
    en_title: "Knowledge Property God",
    en_content: "Genesis 2:15, 16: Knowledge is not a right; knowledge is the property of God.",
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
WHERE t.name = "thought.KNOWLEDGE PROPERTY GOD" AND c.name = "content.KNOWLEDGE PROPERTY GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.KNOWLEDGE PROPERTY GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.KNOWLEDGE PROPERTY GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >KNOWLEDGE PROPERTY GOD" }]->(child);
```
