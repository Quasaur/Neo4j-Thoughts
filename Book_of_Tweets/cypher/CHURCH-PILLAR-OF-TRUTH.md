---
name: "thought.CHURCH PILLAR OF TRUTH"
alias: "Thought: Church Pillar Of Truth"
type: THOUGHT
en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous."
parent: "topic.RELIGION"
tags:
- church
- truth
- pillar
- bible
- religion
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.CHURCH PILLAR OF TRUTH",
    alias: "Thought: Church Pillar Of Truth",
    parent: "topic.RELIGION",
    tags: ['church', 'truth', 'pillar', 'bible', 'religion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHURCH PILLAR OF TRUTH",
    en_title: "Church Pillar Of Truth",
    en_content: "1 Tim. 3:15: The Church of God is the Pillar and Ground of the Truth on Earth, and to attack and criticize her is perilous.",
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
WHERE t.name = "thought.CHURCH PILLAR OF TRUTH" AND c.name = "content.CHURCH PILLAR OF TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH PILLAR OF TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHURCH PILLAR OF TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHURCH PILLAR OF TRUTH" }]->(child);
```
