---
name: "thought.GODS SELF PORTRAIT"
alias: "Thought: Gods Self Portrait"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- jesus
- christ
- portrait
- humanity
- holyspirit
level: 1
neo4j: true
insert: true
---
# Gods Self Portrait

> [!Thought-en]
> Jesus Christ is God's Self Portrait, etched on the canvas of humanity by the Holy Spirit.

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.GODS SELF PORTRAIT",
    alias: "Thought: Gods Self Portrait",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'christ', 'portrait', 'humanity', 'holyspirit'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GODS SELF PORTRAIT",
    en_title: "Gods Self Portrait",
    en_content: "Jesus Christ is God's Self Portrait, etched on the canvas of humanity by the Holy Spirit.",
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
WHERE t.name = "thought.GODS SELF PORTRAIT" AND c.name = "content.GODS SELF PORTRAIT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS SELF PORTRAIT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GODS SELF PORTRAIT"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GODS SELF PORTRAIT" }]->(child);
```