---
name: "thought.WANTING LOVE ONLY"
alias: "Thought: Wanting Love Only"
type: THOUGHT
en_content: "We want to be loved, but we don't want to love...how pathetic."
parent: "topic.ATTITUDE"
tags:
- love
- selfishness
- attitude
- pathetic
- character
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013b)
CREATE (t:THOUGHT {
    name: "thought.WANTING LOVE ONLY",
    alias: "Thought: Wanting Love Only",
    parent: "topic.ATTITUDE",
    tags: ['love', 'selfishness', 'attitude', 'pathetic', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WANTING LOVE ONLY",
    en_title: "Wanting Love Only",
    en_content: "We want to be loved, but we don't want to love...how pathetic.",
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
WHERE t.name = "thought.WANTING LOVE ONLY" AND c.name = "content.WANTING LOVE ONLY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WANTING LOVE ONLY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.WANTING LOVE ONLY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >WANTING LOVE ONLY" }]->(child);
```
