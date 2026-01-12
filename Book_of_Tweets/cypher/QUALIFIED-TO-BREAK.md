---
name: "thought.QUALIFIED TO BREAK"
alias: "Thought: Qualified To Break"
type: THOUGHT
en_content: "The only Person qualified to break me is The One Who has demonstrated Their LOVE for me."
parent: "topic.THE GODHEAD"
tags:
- love
- surrender
- character
- god
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.QUALIFIED TO BREAK",
    alias: "Thought: Qualified To Break",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'surrender', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.QUALIFIED TO BREAK",
    en_title: "Qualified To Break",
    en_content: "The only Person qualified to break me is The One Who has demonstrated Their LOVE for me.",
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
WHERE t.name = "thought.QUALIFIED TO BREAK" AND c.name = "content.QUALIFIED TO BREAK"
MERGE (t)-[:HAS_CONTENT { "name": "edge.QUALIFIED TO BREAK" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.QUALIFIED TO BREAK"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >QUALIFIED TO BREAK" }]->(child);
```
