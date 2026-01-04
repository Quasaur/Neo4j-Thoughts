---
name: "thought.NO ANGER SELFLESSNESS"
alias: "Thought: No Anger Selflessness"
type: THOUGHT
en_content: "There is no anger in selflessness."
parent: "topic.ATTITUDE"
tags:
- selflessness
- anger
- attitude
- peace
- character
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.NO ANGER SELFLESSNESS",
    alias: "Thought: No Anger Selflessness",
    parent: "topic.ATTITUDE",
    tags: ['selflessness', 'anger', 'attitude', 'peace', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NO ANGER SELFLESSNESS",
    en_title: "No Anger Selflessness",
    en_content: "There is no anger in selflessness.",
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
WHERE t.name = "thought.NO ANGER SELFLESSNESS" AND c.name = "content.NO ANGER SELFLESSNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO ANGER SELFLESSNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.NO ANGER SELFLESSNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >NO ANGER SELFLESSNESS" }]->(child);
```
