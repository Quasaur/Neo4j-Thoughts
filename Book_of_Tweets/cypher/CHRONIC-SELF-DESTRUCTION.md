---
name: "thought.CHRONIC SELF DESTRUCTION"
alias: "Thought: Chronic Self Destruction"
type: THOUGHT
en_content: "As a species the homosapien is chronically self-destructive and IT CANNOT STOP ITSELF...therefore God must judge it."
parent: "topic.HUMANITY"
tags:
- humanity
- destruction
- judgment
- failure
- species
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.CHRONIC SELF DESTRUCTION",
    alias: "Thought: Chronic Self Destruction",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'destruction', 'judgment', 'failure', 'species'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRONIC SELF DESTRUCTION",
    en_title: "Chronic Self Destruction",
    en_content: "As a species the homosapien is chronically self-destructive and IT CANNOT STOP ITSELF...therefore God must judge it.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHRONIC SELF DESTRUCTION" AND c.name = "content.CHRONIC SELF DESTRUCTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRONIC SELF DESTRUCTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CHRONIC SELF DESTRUCTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CHRONIC SELF DESTRUCTION" }]->(child);
```
