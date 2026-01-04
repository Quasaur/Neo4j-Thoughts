---
name: "thought.PEOPLE MORE UNFORGIVING"
alias: "Thought: People More Unforgiving"
type: THOUGHT
en_content: "People are FAR MORE unforgiving than God."
parent: "topic.THE GODHEAD"
tags:
- forgiveness
- god
- people
- divinity
level: 1
neo4j: true
insert: true
---
# People More Unforgiving

> [!Thought-en]
> People are FAR MORE unforgiving than God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.PEOPLE MORE UNFORGIVING",
    alias: "Thought: People More Unforgiving",
    parent: "topic.THE GODHEAD",
    tags: ['forgiveness', 'god', 'people', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PEOPLE MORE UNFORGIVING",
    en_title: "People More Unforgiving",
    en_content: "People are FAR MORE unforgiving than God.",
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
WHERE t.name = "thought.PEOPLE MORE UNFORGIVING" AND c.name = "content.PEOPLE MORE UNFORGIVING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PEOPLE MORE UNFORGIVING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.PEOPLE MORE UNFORGIVING"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >PEOPLE MORE UNFORGIVING" }]->(child);
```