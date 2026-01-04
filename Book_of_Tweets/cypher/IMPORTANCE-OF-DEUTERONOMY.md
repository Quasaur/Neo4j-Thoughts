---
name: "thought.IMPORTANCE OF DEUTERONOMY"
alias: "Thought: Importance Of Deuteronomy"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- bible
- truth
- history
- deuteronomy
- law
level: 2
neo4j: true
insert: true
---
# Importance Of Deuteronomy

> [!Thought-en]
> I'm convinced that the most important book of the Old Testament is Deuteronomy, which contains the ENTIRE PANORAMA of Biblical history.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.IMPORTANCE OF DEUTERONOMY",
    alias: "Thought: Importance Of Deuteronomy",
    parent: "topic.TRUTH",
    tags: ['bible', 'truth', 'history', 'deuteronomy', 'law'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMPORTANCE OF DEUTERONOMY",
    en_title: "Importance Of Deuteronomy",
    en_content: "I'm convinced that the most important book of the Old Testament is Deuteronomy, which contains the ENTIRE PANORAMA of Biblical history.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMPORTANCE OF DEUTERONOMY" AND c.name = "content.IMPORTANCE OF DEUTERONOMY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.IMPORTANCE OF DEUTERONOMY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.IMPORTANCE OF DEUTERONOMY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >IMPORTANCE OF DEUTERONOMY" }]->(child);
```