---
name: "thought.PROGRESS AND FAILURE"
alias: "Thought: Progress And Failure"
type: THOUGHT
en_content: "There's no progress without failure."
parent: "topic.WISDOM"
tags:
- wisdom
- progress
- failure
- growth
- truth
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.PROGRESS AND FAILURE",
    alias: "Thought: Progress And Failure",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'progress', 'failure', 'growth', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PROGRESS AND FAILURE",
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

MATCH (t:THOUGHT {name: "thought.PROGRESS AND FAILURE"})
MATCH (c:CONTENT {name: "content.PROGRESS AND FAILURE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PROGRESS AND FAILURE" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.PROGRESS AND FAILURE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >PROGRESS AND FAILURE" }]->(child);
```
