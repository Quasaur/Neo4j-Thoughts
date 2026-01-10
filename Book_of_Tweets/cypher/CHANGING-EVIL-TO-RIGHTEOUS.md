---
name: "thought.CHANGING EVIL TO RIGHTEOUS"
alias: "Thought: Changing Evil To Righteous"
type: THOUGHT
en_content: "God's Other Genius is changing evil people into righteous people!"
parent: "topic.THE GODHEAD"
tags:
- transformation
- grace
- genius
- god
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.CHANGING EVIL TO RIGHTEOUS",
    alias: "Thought: Changing Evil To Righteous",
    parent: "topic.THE GODHEAD",
    tags: ['transformation', 'grace', 'genius', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.CHANGING EVIL TO RIGHTEOUS",
    en_title: "Changing Evil To Righteous",
    en_content: "God's Other Genius is changing evil people into righteous people!",
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
WHERE t.name = "thought.CHANGING EVIL TO RIGHTEOUS" AND c.name = "content.CHANGING EVIL TO RIGHTEOUS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHANGING EVIL TO RIGHTEOUS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.CHANGING EVIL TO RIGHTEOUS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >CHANGING EVIL TO RIGHTEOUS" }]->(child);
```
