---
name: "thought.PRAYER NOT JOB"
alias: "Thought: Prayer Not Job"
type: THOUGHT
en_content: "Prayer was never meant to be a job."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- work
- spirituality
- connection
- attitude
level: 2
neo4j: true
insert: true
---
# Prayer Not Job

> [!Thought-en]
> Prayer was never meant to be a job.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.PRAYER NOT JOB",
    alias: "Thought: Prayer Not Job",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'work', 'spirituality', 'connection', 'attitude'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER NOT JOB",
    en_title: "Prayer Not Job",
    en_content: "Prayer was never meant to be a job.",
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
WHERE t.name = "thought.PRAYER NOT JOB" AND c.name = "content.PRAYER NOT JOB"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER NOT JOB" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER NOT JOB"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER NOT JOB" }]->(child);
```