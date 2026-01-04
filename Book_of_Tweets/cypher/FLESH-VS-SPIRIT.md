---
name: "thought.FLESH VS SPIRIT"
alias: "Thought: Flesh Vs Spirit"
type: THOUGHT
en_content: "The flesh is too stupid to be spiritual; it must be crucified with Christ and brought in subjection by the Love of God to the Spirit of God."
parent: "topic.SPIRITUALITY"
tags:
- flesh
- spirit
- crucifixion
- subjection
- sanctification
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.FLESH VS SPIRIT",
    alias: "Thought: Flesh Vs Spirit",
    parent: "topic.SPIRITUALITY",
    tags: ['flesh', 'spirit', 'crucifixion', 'subjection', 'sanctification'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FLESH VS SPIRIT",
    en_title: "Flesh Vs Spirit",
    en_content: "The flesh is too stupid to be spiritual; it must be crucified with Christ and brought in subjection by the Love of God to the Spirit of God.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FLESH VS SPIRIT" AND c.name = "content.FLESH VS SPIRIT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FLESH VS SPIRIT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FLESH VS SPIRIT"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FLESH VS SPIRIT" }]->(child);
```
