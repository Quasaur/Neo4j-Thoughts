---
name: "thought.BUILD ON THE ROCK"
alias: "Thought: Build On The Rock"
type: THOUGHT
en_content: "You can build WITH Gold, but you can't build ON Gold; you must build on The ROCK...it's not as shiny, but it's a lot stronger!"
parent: "topic.SPIRITUALITY"
tags:
- rock
- gold
- foundation
- spirituality
- strength
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.BUILD ON THE ROCK",
    alias: "Thought: Build On The Rock",
    parent: "topic.SPIRITUALITY",
    tags: ['rock', 'gold', 'foundation', 'spirituality', 'strength'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BUILD ON THE ROCK",
    en_title: "Build On The Rock",
    en_content: "You can build WITH Gold, but you can't build ON Gold; you must build on The ROCK...it's not as shiny, but it's a lot stronger!",
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
WHERE t.name = "thought.BUILD ON THE ROCK" AND c.name = "content.BUILD ON THE ROCK"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BUILD ON THE ROCK" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.BUILD ON THE ROCK"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >BUILD ON THE ROCK" }]->(child);
```
