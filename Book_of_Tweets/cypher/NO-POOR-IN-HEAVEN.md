---
name: "thought.NO POOR IN HEAVEN"
alias: "Thought: No Poor In Heaven"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- heaven
- poverty
- abundance
- eternity
- provision
level: 2
neo4j: true
insert: true
---
# No Poor In Heaven

> [!Thought-en]
> There are no poor in Heaven.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NO POOR IN HEAVEN",
    alias: "Thought: No Poor In Heaven",
    parent: "topic.SPIRITUALITY",
    tags: ['heaven', 'poverty', 'abundance', 'eternity', 'provision'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NO POOR IN HEAVEN",
    en_title: "No Poor In Heaven",
    en_content: "There are no poor in Heaven.",
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
WHERE t.name = "thought.NO POOR IN HEAVEN" AND c.name = "content.NO POOR IN HEAVEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO POOR IN HEAVEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.NO POOR IN HEAVEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >NO POOR IN HEAVEN" }]->(child);
```