---
name: "thought.INTERIOR MISSISSIPPI"
alias: "Thought: Interior Mississippi"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- society
- geography
- culture
- morality
- reflection
level: 3
neo4j: true
insert: true
---
# Interior Mississippi

> [!Thought-en]
> "You know what they say: 'Between Pittsburgh and Philadelphia is Mississippi!'" -- Anonymous

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.INTERIOR MISSISSIPPI",
    alias: "Thought: Interior Mississippi",
    parent: "topic.MORALITY",
    tags: ['society', 'geography', 'culture', 'morality', 'reflection'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INTERIOR MISSISSIPPI",
    en_title: "Interior Mississippi",
    en_content: "\"You know what they say: 'Between Pittsburgh and Philadelphia is Mississippi!'\" -- Anonymous",
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
WHERE t.name = "thought.INTERIOR MISSISSIPPI" AND c.name = "content.INTERIOR MISSISSIPPI"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTERIOR MISSISSIPPI" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.INTERIOR MISSISSIPPI"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >INTERIOR MISSISSIPPI" }]->(child);
```