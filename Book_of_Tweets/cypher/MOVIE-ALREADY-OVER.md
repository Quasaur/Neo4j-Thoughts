---
name: "thought.MOVIE ALREADY OVER"
alias: "Thought: Movie Already Over"
type: THOUGHT
en_content: "The Bible says the movie is already over...roll the credits!"
parent: "topic.RELIGION"
tags:
- prophecy
- bible
- time
- judgment
- eternity
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Mar-2013)
CREATE (t:THOUGHT {
    name: "thought.MOVIE ALREADY OVER",
    alias: "Thought: Movie Already Over",
    parent: "topic.RELIGION",
    tags: ['prophecy', 'bible', 'time', 'judgment', 'eternity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MOVIE ALREADY OVER",
    en_title: "Movie Already Over",
    en_content: "The Bible says the movie is already over...roll the credits!",
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
WHERE t.name = "thought.MOVIE ALREADY OVER" AND c.name = "content.MOVIE ALREADY OVER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOVIE ALREADY OVER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.MOVIE ALREADY OVER"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >MOVIE ALREADY OVER" }]->(child);
```
