---
name: "thought.ENDANGERED BLACK MEN"
alias: "Thought: Endangered Black Men"
type: THOUGHT
en_content: "African American men have ALWAYS been the targets of genocide...we are an ENDANGERED SPECIES."
parent: "topic.HUMANITY"
tags:
- race
- genocide
- target
- humanity
- justice
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.ENDANGERED BLACK MEN",
    alias: "Thought: Endangered Black Men",
    parent: "topic.HUMANITY",
    tags: ['race', 'genocide', 'target', 'humanity', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ENDANGERED BLACK MEN",
    en_title: "Endangered Black Men",
    en_content: "African American men have ALWAYS been the targets of genocide...we are an ENDANGERED SPECIES.",
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
WHERE t.name = "thought.ENDANGERED BLACK MEN" AND c.name = "content.ENDANGERED BLACK MEN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ENDANGERED BLACK MEN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.ENDANGERED BLACK MEN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >ENDANGERED BLACK MEN" }]->(child);
```
