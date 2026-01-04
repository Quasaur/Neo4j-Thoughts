---
name: "thought.UNIVERSAL MERCY REQUIREMENT"
alias: "Thought: Universal Mercy Requirement"
type: THOUGHT
en_content: "God has to have mercy on everybody in order to save anybody."
parent: "topic.GRACE"
tags:
- mercy
- grace
- salvation
- humanity
- god
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.UNIVERSAL MERCY REQUIREMENT",
    alias: "Thought: Universal Mercy Requirement",
    parent: "topic.GRACE",
    tags: ['mercy', 'grace', 'salvation', 'humanity', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNIVERSAL MERCY REQUIREMENT",
    en_title: "Universal Mercy Requirement",
    en_content: "God has to have mercy on everybody in order to save anybody.",
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
WHERE t.name = "thought.UNIVERSAL MERCY REQUIREMENT" AND c.name = "content.UNIVERSAL MERCY REQUIREMENT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNIVERSAL MERCY REQUIREMENT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.UNIVERSAL MERCY REQUIREMENT"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >UNIVERSAL MERCY REQUIREMENT" }]->(child);
```
