---
type: THOUGHT
name: "thought.ENDING"
alias: "Thought: ENDING"
parent: "topic.APOCALYPSE"
en_content: "\"
 es_title: "FINAL"
 es_content: ""
 fr_title: "FIN"
 fr_content: ""
 hi_title: "ख़त्म होना"
 hi_content: ""
 zh_title: "jié shù"
 zh_content: ""
tags: ["ending", "bible", "apocalypse", "judgment", "newjerusalem"]
ptopic: "[[topic-APOCALYPSE]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ENDING",
    alias: "Thought: ENDING",
    parent: "topic.APOCALYPSE",
    tags: ["ending", "bible", "apocalypse", "judgment", "newjerusalem"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ENDING",
    ctype: "THOUGHT",
    en_title: "ENDING",
    en_content: "\",
 es_title: "FINAL",
 es_content: "",
 fr_title: "FIN",
 fr_content: "",
 hi_title: "ख़त्म होना",
 hi_content: "",
 zh_title: "jié shù",
 zh_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ENDING" AND c.name = "content.ENDING"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ENDING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.APOCALYPSE" AND child.name = "thought.ENDING"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.APOCALYPSE->ENDING"}]->(child);