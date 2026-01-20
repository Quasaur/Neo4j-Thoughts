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
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Mar-2013)
CREATE (t:THOUGHT {
    name: "thought.MOVIE ALREADY OVER",
    alias: "Thought: Movie Already Over",
    parent: "topic.RELIGION",
    tags: ['prophecy', 'bible', 'time', 'judgment', 'eternity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MOVIE ALREADY OVER",
    en_title: "Movie Already Over",
    en_content: "The Bible says the movie is already over...roll the credits!",
    es_title: "La Película Ya Terminó",
    es_content: "La Biblia dice que la película ya terminó... ¡pasen los créditos!",
    fr_title: "Le Film Est Déjà Fini",
    fr_content: "La Bible dit que le film est déjà fini... passez le générique !",
    hi_title: "फिल्म पहले से ही समाप्त",
    hi_content: "बाइबल कहती है कि फिल्म पहले से ही समाप्त हो गई है... क्रेडिट रोल करें!",
    zh_title: "Dianying Yijing Jieshu",
    zh_content: "Shengjing shuo dianying yijing jieshu le... gunchu zimu ba!"
});

MATCH (t:THOUGHT {name: "thought.MOVIE ALREADY OVER"})
MATCH (c:CONTENT {name: "content.MOVIE ALREADY OVER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MOVIE ALREADY OVER" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.MOVIE ALREADY OVER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >MOVIE ALREADY OVER" }]->(child);
```
