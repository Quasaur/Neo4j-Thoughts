---
name: "thought.PRICE OF PRIDE"
alias: "Thought: Price Of Pride"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- pride
- killing
- price
- race
- morality
level: 3
neo4j: true
insert: true
---
# Price Of Pride

> [!Thought-en]
> At what point in history did African American men decide that pride was worth the price of killing each other??

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012e)
CREATE (t:THOUGHT {
    name: "thought.PRICE OF PRIDE",
    alias: "Thought: Price Of Pride",
    parent: "topic.MORALITY",
    tags: ['pride', 'killing', 'price', 'race', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRICE OF PRIDE",
    en_title: "Price Of Pride",
    en_content: "At what point in history did African American men decide that pride was worth the price of killing each other??",
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
WHERE t.name = "thought.PRICE OF PRIDE" AND c.name = "content.PRICE OF PRIDE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRICE OF PRIDE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.PRICE OF PRIDE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >PRICE OF PRIDE" }]->(child);
```