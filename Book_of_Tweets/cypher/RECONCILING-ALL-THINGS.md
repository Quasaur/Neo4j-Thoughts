---
name: "thought.RECONCILING ALL THINGS"
alias: "Thought: Reconciling All Things"
type: THOUGHT
en_content: "1st Corinthians 15:24-28: God is #reconciling and consolidating all things into Christ."
parent: "topic.THE GODHEAD"
tags:
- reconciliation
- christ
- sovereignty
- consolidation
- divinity
level: 1
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.RECONCILING ALL THINGS",
    alias: "Thought: Reconciling All Things",
    parent: "topic.THE GODHEAD",
    tags: ["reconciliation", "christ", "sovereignty", "consolidation", "divinity"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.RECONCILING ALL THINGS",
    en_title: "Reconciling All Things",
    en_content: "1st Corinthians 15:24-28: God is #reconciling and consolidating all things into Christ.",
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
WHERE t.name = "thought.RECONCILING ALL THINGS" AND c.name = "content.RECONCILING ALL THINGS"
MERGE (t)-[:HAS_CONTENT {name: "edge.RECONCILING ALL THINGS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.RECONCILING ALL THINGS"
MERGE (parent)-[:HAS_THOUGHT {name: "THE GODHEAD >RECONCILING ALL THINGS"}]->(child);
```
