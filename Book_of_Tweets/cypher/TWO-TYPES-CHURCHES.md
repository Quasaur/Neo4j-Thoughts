---
name: "thought.TWO TYPES CHURCHES"
alias: "Thought: Two Types Churches"
type: THOUGHT
parent: "topic.RELIGION"
tags:
- church
- eternity
- election
- religion
- institutions
level: 3
neo4j: true
insert: true
---
# Two Types Churches

> [!Thought-en]
> There are two churches: (1) the institutionalized church, and (2) the REAL church elected by God; one is temporary, one is eternal.

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.TWO TYPES CHURCHES",
    alias: "Thought: Two Types Churches",
    parent: "topic.RELIGION",
    tags: ['church', 'eternity', 'election', 'religion', 'institutions'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TWO TYPES CHURCHES",
    en_title: "Two Types Churches",
    en_content: "There are two churches: (1) the institutionalized church, and (2) the REAL church elected by God; one is temporary, one is eternal.",
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
WHERE t.name = "thought.TWO TYPES CHURCHES" AND c.name = "content.TWO TYPES CHURCHES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TWO TYPES CHURCHES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.TWO TYPES CHURCHES"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >TWO TYPES CHURCHES" }]->(child);
```