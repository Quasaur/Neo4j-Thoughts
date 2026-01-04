---
name: "thought.REJECTED TRUTH WEIGHT"
alias: "Thought: Rejected Truth Weight"
type: THOUGHT
en_content: "The World will perish...crushed under the weight of the Truth it has rejected."
parent: "topic.TRUTH"
tags:
- truth
- rejection
- judgment
- world
- weight
level: 2
neo4j: true
insert: true
---
# Rejected Truth Weight

> [!Thought-en]
> The World will perish...crushed under the weight of the Truth it has rejected.

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-May-2012c)
CREATE (t:THOUGHT {
    name: "thought.REJECTED TRUTH WEIGHT",
    alias: "Thought: Rejected Truth Weight",
    parent: "topic.TRUTH",
    tags: ['truth', 'rejection', 'judgment', 'world', 'weight'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REJECTED TRUTH WEIGHT",
    en_title: "Rejected Truth Weight",
    en_content: "The World will perish...crushed under the weight of the Truth it has rejected.",
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
WHERE t.name = "thought.REJECTED TRUTH WEIGHT" AND c.name = "content.REJECTED TRUTH WEIGHT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJECTED TRUTH WEIGHT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.REJECTED TRUTH WEIGHT"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >REJECTED TRUTH WEIGHT" }]->(child);
```