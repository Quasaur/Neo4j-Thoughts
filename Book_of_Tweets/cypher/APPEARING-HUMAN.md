---
name: "thought.APPEARING HUMAN"
alias: "Thought: Appearing Human"
type: THOUGHT
en_content: "Beware of those who appear human, but ain't!"
parent: "topic.EVIL"
tags:
- deception
- evil
- appearance
- caution
- humanity
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.APPEARING HUMAN",
    alias: "Thought: Appearing Human",
    parent: "topic.EVIL",
    tags: ['deception', 'evil', 'appearance', 'caution', 'humanity'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.APPEARING HUMAN",
    en_title: "Appearing Human",
    en_content: "Beware of those who appear human, but ain't!",
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
WHERE t.name = "thought.APPEARING HUMAN" AND c.name = "content.APPEARING HUMAN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.APPEARING HUMAN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.APPEARING HUMAN"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >APPEARING HUMAN" }]->(child);
```
