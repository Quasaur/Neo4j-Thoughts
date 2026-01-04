---
name: "thought.MARRIAGE RELIGIOUS INSTITUTION"
alias: "Thought: Marriage Religious Institution"
type: THOUGHT
en_content: "Congress shall make no law regarding the practice of religion...marriage is a RELIGIOUS institution!"
parent: "topic.RELIGION"
tags:
- marriage
- religion
- law
- institution
- history
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Sep-2013)
CREATE (t:THOUGHT {
    name: "thought.MARRIAGE RELIGIOUS INSTITUTION",
    alias: "Thought: Marriage Religious Institution",
    parent: "topic.RELIGION",
    tags: ['marriage', 'religion', 'law', 'institution', 'history'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MARRIAGE RELIGIOUS INSTITUTION",
    en_title: "Marriage Religious Institution",
    en_content: "Congress shall make no law regarding the practice of religion...marriage is a RELIGIOUS institution!",
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
WHERE t.name = "thought.MARRIAGE RELIGIOUS INSTITUTION" AND c.name = "content.MARRIAGE RELIGIOUS INSTITUTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MARRIAGE RELIGIOUS INSTITUTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.MARRIAGE RELIGIOUS INSTITUTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >MARRIAGE RELIGIOUS INSTITUTION" }]->(child);
```
