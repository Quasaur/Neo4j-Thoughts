---
name: "thought.CORRUPTION WITHOUT DEATH"
alias: "Thought: Corruption Without Death"
type: THOUGHT
en_content: "Watched movie \"In Time\"; without death, humanity would be even more hideously corrupt than it is now."
parent: "topic.HUMANITY"
tags:
- death
- corruption
- humanity
- character
- morality
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CORRUPTION WITHOUT DEATH",
    alias: "Thought: Corruption Without Death",
    parent: "topic.HUMANITY",
    tags: ['death', 'corruption', 'humanity', 'character', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CORRUPTION WITHOUT DEATH",
    en_title: "Corruption Without Death",
    en_content: "Watched movie \"In Time\"; without death, humanity would be even more hideously corrupt than it is now.",
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
WHERE t.name = "thought.CORRUPTION WITHOUT DEATH" AND c.name = "content.CORRUPTION WITHOUT DEATH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CORRUPTION WITHOUT DEATH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CORRUPTION WITHOUT DEATH"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CORRUPTION WITHOUT DEATH" }]->(child);
```
