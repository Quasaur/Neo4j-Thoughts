---
name: "thought.FAST LANE BLIND SPOTS"
alias: "Thought: Fast Lane Blind Spots"
type: THOUGHT
en_content: "If you're living in the fast lane, watch your blind spots."
parent: "topic.WISDOM"
tags:
- wisdom
- life
- danger
- awareness
- caution
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.FAST LANE BLIND SPOTS",
    alias: "Thought: Fast Lane Blind Spots",
    parent: "topic.WISDOM",
    tags: ['wisdom', 'life', 'danger', 'awareness', 'caution'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FAST LANE BLIND SPOTS",
    en_title: "Fast Lane Blind Spots",
    en_content: "If you're living in the fast lane, watch your blind spots.",
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
WHERE t.name = "thought.FAST LANE BLIND SPOTS" AND c.name = "content.FAST LANE BLIND SPOTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAST LANE BLIND SPOTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.FAST LANE BLIND SPOTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM >FAST LANE BLIND SPOTS" }]->(child);
```
