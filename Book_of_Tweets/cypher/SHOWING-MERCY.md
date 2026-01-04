---
name: "thought.SHOWING MERCY"
alias: "Thought: Showing Mercy"
type: THOUGHT
en_content: "Everybody wants Mercy...few show Mercy."
parent: "topic.MORALITY"
tags:
- mercy
- morality
- character
- compassion
- judgment
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.SHOWING MERCY",
    alias: "Thought: Showing Mercy",
    parent: "topic.MORALITY",
    tags: ['mercy', 'morality', 'character', 'compassion', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOWING MERCY",
    en_title: "Showing Mercy",
    en_content: "Everybody wants Mercy...few show Mercy.",
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
WHERE t.name = "thought.SHOWING MERCY" AND c.name = "content.SHOWING MERCY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOWING MERCY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SHOWING MERCY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SHOWING MERCY" }]->(child);
```
