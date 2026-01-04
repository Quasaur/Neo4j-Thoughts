---
name: "thought.DAMNING THE ARROGANT"
alias: "Thought: Damning The Arrogant"
type: THOUGHT
en_content: "How does God damn a sinner? By letting them prosper in their arrogance."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- arrogance
- prosperity
- sovereignty
- god
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-May-2012)
CREATE (t:THOUGHT {
    name: "thought.DAMNING THE ARROGANT",
    alias: "Thought: Damning The Arrogant",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'arrogance', 'prosperity', 'sovereignty', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DAMNING THE ARROGANT",
    en_title: "Damning The Arrogant",
    en_content: "How does God damn a sinner? By letting them prosper in their arrogance.",
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
WHERE t.name = "thought.DAMNING THE ARROGANT" AND c.name = "content.DAMNING THE ARROGANT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DAMNING THE ARROGANT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.DAMNING THE ARROGANT"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >DAMNING THE ARROGANT" }]->(child);
```
