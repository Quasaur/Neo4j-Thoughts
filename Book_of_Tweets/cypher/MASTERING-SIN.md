---
name: "thought.MASTERING SIN"
alias: "Thought: Mastering Sin"
type: THOUGHT
en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin."
parent: "topic.MORALITY"
tags:
- sin
- mastery
- morality
- responsibility
- victory
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Sep-2010)
CREATE (t:THOUGHT {
    name: "thought.MASTERING SIN",
    alias: "Thought: Mastering Sin",
    parent: "topic.MORALITY",
    tags: ['sin', 'mastery', 'morality', 'responsibility', 'victory'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MASTERING SIN",
    en_title: "Mastering Sin",
    en_content: "Genesis 4:6,7 God doesn't expect us to eradicate sin (that's His Job)...but He does expect us to master sin.",
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
WHERE t.name = "thought.MASTERING SIN" AND c.name = "content.MASTERING SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MASTERING SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.MASTERING SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >MASTERING SIN" }]->(child);
```
