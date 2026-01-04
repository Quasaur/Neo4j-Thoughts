---
name: "thought.PRAYER HAWAIIAN VACATION"
alias: "Thought: Prayer Hawaiian Vacation"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- prayer
- rest
- vacation
- spirituality
- joy
level: 2
neo4j: true
insert: true
---
# Prayer Hawaiian Vacation

> [!Thought-en]
> Prayer is my Hawaiian vacation.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.PRAYER HAWAIIAN VACATION",
    alias: "Thought: Prayer Hawaiian Vacation",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'rest', 'vacation', 'spirituality', 'joy'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER HAWAIIAN VACATION",
    en_title: "Prayer Hawaiian Vacation",
    en_content: "Prayer is my Hawaiian vacation.",
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
WHERE t.name = "thought.PRAYER HAWAIIAN VACATION" AND c.name = "content.PRAYER HAWAIIAN VACATION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER HAWAIIAN VACATION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER HAWAIIAN VACATION"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER HAWAIIAN VACATION" }]->(child);
```