---
name: "thought.ALIGNING THROUGH PRAYER"
alias: "Thought: Aligning Through Prayer"
type: THOUGHT
en_content: "The purpose of prayer is not just to get God to do stuff, but to align myself with what God is doing!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- alignment
- will
- purpose
level: 2
neo4j: true
insert: true
---
# Aligning Through Prayer

> [!Thought-en]
> The purpose of prayer is not just to get God to do stuff, but to align myself with what God is doing!

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.ALIGNING THROUGH PRAYER",
    alias: "Thought: Aligning Through Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'alignment', 'will', 'purpose'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ALIGNING THROUGH PRAYER",
    en_title: "Aligning Through Prayer",
    en_content: "The purpose of prayer is not just to get God to do stuff, but to align myself with what God is doing!",
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
WHERE t.name = "thought.ALIGNING THROUGH PRAYER" AND c.name = "content.ALIGNING THROUGH PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALIGNING THROUGH PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.ALIGNING THROUGH PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >ALIGNING THROUGH PRAYER" }]->(child);
```