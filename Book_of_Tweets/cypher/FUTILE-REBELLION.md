---
name: "thought.FUTILE REBELLION"
alias: "Thought: Futile Rebellion"
type: THOUGHT
en_content: "Rebellion against God is futile!"
parent: "topic.HUMANITY"
tags:
- rebellion
- futility
- humanity
- god
- sovereignty
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jan-2012a)
CREATE (t:THOUGHT {
    name: "thought.FUTILE REBELLION",
    alias: "Thought: Futile Rebellion",
    parent: "topic.HUMANITY",
    tags: ['rebellion', 'futility', 'humanity', 'god', 'sovereignty'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FUTILE REBELLION",
    en_title: "Futile Rebellion",
    en_content: "Rebellion against God is futile!",
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
WHERE t.name = "thought.FUTILE REBELLION" AND c.name = "content.FUTILE REBELLION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FUTILE REBELLION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.FUTILE REBELLION"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >FUTILE REBELLION" }]->(child);
```
