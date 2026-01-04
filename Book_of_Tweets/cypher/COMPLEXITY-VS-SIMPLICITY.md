---
name: "thought.COMPLEXITY VS SIMPLICITY"
alias: "Thought: Complexity Vs Simplicity"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- complexity
- simplicity
- science
- law
- truth
level: 2
neo4j: true
insert: true
---
# Complexity Vs Simplicity

> [!Thought-en]
> There is no "natural law" that would bring complexity out of simplicity!

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.COMPLEXITY VS SIMPLICITY",
    alias: "Thought: Complexity Vs Simplicity",
    parent: "topic.TRUTH",
    tags: ['complexity', 'simplicity', 'science', 'law', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COMPLEXITY VS SIMPLICITY",
    en_title: "Complexity Vs Simplicity",
    en_content: "There is no \"natural law\" that would bring complexity out of simplicity!",
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
WHERE t.name = "thought.COMPLEXITY VS SIMPLICITY" AND c.name = "content.COMPLEXITY VS SIMPLICITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMPLEXITY VS SIMPLICITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.COMPLEXITY VS SIMPLICITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >COMPLEXITY VS SIMPLICITY" }]->(child);
```