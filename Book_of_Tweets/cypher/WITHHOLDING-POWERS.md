---
name: "thought.WITHHOLDING POWERS"
alias: "Thought: Withholding Powers"
type: THOUGHT
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- power
- glory
- sovereignty
- character
- responsibility
level: 2
neo4j: true
insert: true
---
# Withholding Powers

> [!Thought-en]
> God withholds powers from us because we do not give Him glory for powers already bestowed.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.WITHHOLDING POWERS",
    alias: "Thought: Withholding Powers",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['power', 'glory', 'sovereignty', 'character', 'responsibility'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WITHHOLDING POWERS",
    en_title: "Withholding Powers",
    en_content: "God withholds powers from us because we do not give Him glory for powers already bestowed.",
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
WHERE t.name = "thought.WITHHOLDING POWERS" AND c.name = "content.WITHHOLDING POWERS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WITHHOLDING POWERS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.WITHHOLDING POWERS"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >WITHHOLDING POWERS" }]->(child);
```