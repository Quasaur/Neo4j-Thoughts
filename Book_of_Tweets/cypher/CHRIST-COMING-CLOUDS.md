---
name: "thought.CHRIST COMING CLOUDS"
alias: "Thought: Christ Coming Clouds"
type: THOUGHT
en_content: "History is going to play out just as the Bible says; what are you going to do when you see Christ coming in the clouds of Heaven?"
parent: "topic.RELIGION"
tags:
- prophecy
- jesus
- return
- eternity
- judgment
level: 3
neo4j: true
insert: true
---
# Christ Coming Clouds

> [!Thought-en]
> History is going to play out just as the Bible says; what are you going to do when you see Christ coming in the clouds of Heaven?

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Jun-2012)
CREATE (t:THOUGHT {
    name: "thought.CHRIST COMING CLOUDS",
    alias: "Thought: Christ Coming Clouds",
    parent: "topic.RELIGION",
    tags: ['prophecy', 'jesus', 'return', 'eternity', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRIST COMING CLOUDS",
    en_title: "Christ Coming Clouds",
    en_content: "History is going to play out just as the Bible says; what are you going to do when you see Christ coming in the clouds of Heaven?",
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
WHERE t.name = "thought.CHRIST COMING CLOUDS" AND c.name = "content.CHRIST COMING CLOUDS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRIST COMING CLOUDS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHRIST COMING CLOUDS"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHRIST COMING CLOUDS" }]->(child);
```