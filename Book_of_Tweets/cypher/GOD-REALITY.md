---
name: "thought.GOD REALITY"
alias: "Thought: God Reality"
type: THOUGHT
en_content: "As I was watching TV I realized: God is real...we're just cartoon characters compared to Him!"
parent: "topic.THE GODHEAD"
tags:
- god
- reality
- perspective
- nature_of_god
- divinity
level: 1
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD REALITY",
    alias: "Thought: God Reality",
    parent: "topic.THE GODHEAD",
    tags: ["god", "reality", "perspective", "nature_of_god", "divinity"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD REALITY",
    en_title: "God Reality",
    en_content: "As I was watching TV I realized: God is real...we're just cartoon characters compared to Him!",
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
WHERE t.name = "thought.GOD REALITY" AND c.name = "content.GOD REALITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD REALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD REALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "THE GODHEAD >GOD REALITY"}]->(child);
```
