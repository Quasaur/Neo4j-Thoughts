---
name: "thought.WANTING DECEPTION"
alias: "Thought: Wanting Deception"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- deception
- satan
- bible
- humanity
- truth
level: 2
neo4j: true
insert: true
---
# Wanting Deception

> [!Thought-en]
> The Bible says that Satan has deceived us all...and we want to be deceived!

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.WANTING DECEPTION",
    alias: "Thought: Wanting Deception",
    parent: "topic.TRUTH",
    tags: ['deception', 'satan', 'bible', 'humanity', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WANTING DECEPTION",
    en_title: "Wanting Deception",
    en_content: "The Bible says that Satan has deceived us all...and we want to be deceived!",
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
WHERE t.name = "thought.WANTING DECEPTION" AND c.name = "content.WANTING DECEPTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WANTING DECEPTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.WANTING DECEPTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >WANTING DECEPTION" }]->(child);
```