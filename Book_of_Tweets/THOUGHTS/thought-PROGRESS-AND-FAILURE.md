---
type: THOUGHT
name: "thought.PROGRESS AND FAILURE"
alias: "Thought: Progress And Failure"
parent: "topic.WISDOM"
en_content: "There's no progress without failure."
tags: ["wisdom", "progress", "failure", "growth", "truth"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Sep-2011)
CREATE (t:THOUGHT {    name: "thought.PROGRESS AND FAILURE",
    alias: "Thought: Progress And Failure",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'progress', 'failure', 'growth', 'truth'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PROGRESS AND FAILURE",
    ctype: "THOUGHT",
    en_title: "Progress And Failure",
    en_content: "There's no progress without failure.",
    es_title: "Progreso Y Fracaso",
    es_content: "No hay progreso sin fracaso.",
    fr_title: "Progrès Et Échec",
    fr_content: "Il n'y a pas de progrès sans échec.",
    hi_title: "प्रगति और असफलता",
    hi_content: "असफलता के बिना कोई प्रगति नहीं होती।",
    zh_title: "Jinbu Yu Shibai",
    zh_content: "Mei you shibai jiu mei you jinbu."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PROGRESS AND FAILURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->PROGRESS AND FAILURE"
RETURN t, parent;
```
