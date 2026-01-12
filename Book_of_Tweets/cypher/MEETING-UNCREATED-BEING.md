---
name: "thought.MEETING UNCREATED BEING"
alias: "Thought: Meeting Uncreated Being"
type: THOUGHT
en_content: "You haven't lived till you've met An Uncreated Being!"
parent: "topic.THE GODHEAD"
tags:
- encounter
- uncreated
- life
- god
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Nov-2012)
CREATE (t:THOUGHT {
    name: "thought.MEETING UNCREATED BEING",
    alias: "Thought: Meeting Uncreated Being",
    parent: "topic.THE GODHEAD",
    tags: ['encounter', 'uncreated', 'life', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MEETING UNCREATED BEING",
    en_title: "Meeting Uncreated Being",
    en_content: "You haven't lived till you've met An Uncreated Being!",
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
WHERE t.name = "thought.MEETING UNCREATED BEING" AND c.name = "content.MEETING UNCREATED BEING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MEETING UNCREATED BEING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MEETING UNCREATED BEING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MEETING UNCREATED BEING" }]->(child);
```
