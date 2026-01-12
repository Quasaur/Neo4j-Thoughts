---
name: "thought.SHERBERT AND BLOWTORCH"
alias: "Thought: Sherbert And Blowtorch"
type: THOUGHT
en_content: "You can't make sherbert with a blowtorch."
parent: "topic.WISDOM"
tags:
- wisdom
- logic
- metaphor
- patience
- methodology
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Jan-2011)
CREATE (t:THOUGHT {
    name: "thought.SHERBERT AND BLOWTORCH",
    alias: "Thought: Sherbert And Blowtorch",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'logic', 'metaphor', 'patience', 'methodology'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHERBERT AND BLOWTORCH",
    en_title: "Sherbert And Blowtorch",
    en_content: "You can't make sherbert with a blowtorch.",
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
WHERE t.name = "thought.SHERBERT AND BLOWTORCH" AND c.name = "content.SHERBERT AND BLOWTORCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHERBERT AND BLOWTORCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.SHERBERT AND BLOWTORCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >SHERBERT AND BLOWTORCH" }]->(child);
```
