---
name: "thought.RECREATING INTENT"
alias: "Thought: Recreating Intent"
type: THOUGHT
en_content: "Fear of judgment will change our behavior...but not our hearts. Only the Love of Christ can recreate my intent."
parent: "topic.GRACE"
tags:
- love
- transformation
- heart
- grace
- salvation
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011a)
CREATE (t:THOUGHT {
    name: "thought.RECREATING INTENT",
    alias: "Thought: Recreating Intent",
    parent: "topic.GRACE",
    tags: ['love', 'transformation', 'heart', 'grace', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RECREATING INTENT",
    en_title: "Recreating Intent",
    en_content: "Fear of judgment will change our behavior...but not our hearts. Only the Love of Christ can recreate my intent.",
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
WHERE t.name = "thought.RECREATING INTENT" AND c.name = "content.RECREATING INTENT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECREATING INTENT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.RECREATING INTENT"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >RECREATING INTENT" }]->(child);
```
