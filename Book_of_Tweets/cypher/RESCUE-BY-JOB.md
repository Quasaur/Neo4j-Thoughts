---
name: "thought.RESCUE BY JOB"
alias: "Thought: Rescue By Job"
type: THOUGHT
en_content: "I wish to publicly thank God for rescuing us with a job that kept a roof over our heads and the lights on...Jesus is HOT STUFF!!!"
parent: "topic.SPIRITUALITY"
tags:
- provision
- miracle
- gratitude
- work
- god
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.RESCUE BY JOB",
    alias: "Thought: Rescue By Job",
    parent: "topic.SPIRITUALITY",
    tags: ['provision', 'miracle', 'gratitude', 'work', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.RESCUE BY JOB",
    en_title: "Rescue By Job",
    en_content: "I wish to publicly thank God for rescuing us with a job that kept a roof over our heads and the lights on...Jesus is HOT STUFF!!!",
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
WHERE t.name = "thought.RESCUE BY JOB" AND c.name = "content.RESCUE BY JOB"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESCUE BY JOB" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.RESCUE BY JOB"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >RESCUE BY JOB" }]->(child);
```
