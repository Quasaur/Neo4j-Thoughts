---
name: "thought.NOTHING NEW TRUTH"
alias: "Thought: Nothing New Truth"
type: THOUGHT
en_content: "There is nothing new about Truth."
parent: "topic.TRUTH"
tags:
- truth
- antiquity
- consistency
- philosophy
- reality
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.NOTHING NEW TRUTH",
    alias: "Thought: Nothing New Truth",
    parent: "topic.TRUTH",
    tags: ['truth', 'antiquity', 'consistency', 'philosophy', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.NOTHING NEW TRUTH",
    en_title: "Nothing New Truth",
    en_content: "There is nothing new about Truth.",
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
WHERE t.name = "thought.NOTHING NEW TRUTH" AND c.name = "content.NOTHING NEW TRUTH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING NEW TRUTH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.NOTHING NEW TRUTH"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >NOTHING NEW TRUTH" }]->(child);
```
