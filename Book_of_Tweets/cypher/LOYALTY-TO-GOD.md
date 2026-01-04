---
name: "thought.LOYALTY TO GOD"
alias: "Thought: Loyalty To God"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- loyalty
- devotion
- spirituality
- commitment
- sacrifice
level: 2
neo4j: true
insert: true
---
# Loyalty To God

> [!Thought-en]
> What pleases God? Loyalty...at whatever cost to yourself, your family or your friends.

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.LOYALTY TO GOD",
    alias: "Thought: Loyalty To God",
    parent: "topic.SPIRITUALITY",
    tags: ['loyalty', 'devotion', 'spirituality', 'commitment', 'sacrifice'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LOYALTY TO GOD",
    en_title: "Loyalty To God",
    en_content: "What pleases God? Loyalty...at whatever cost to yourself, your family or your friends.",
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
WHERE t.name = "thought.LOYALTY TO GOD" AND c.name = "content.LOYALTY TO GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOYALTY TO GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.LOYALTY TO GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LOYALTY TO GOD" }]->(child);
```