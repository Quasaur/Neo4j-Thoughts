---
name: "thought.TERRIBLE SECRETS"
alias: "Thought: Terrible Secrets"
type: THOUGHT
en_content: "Secrets can be terrible things."
parent: "topic.ATTITUDE"
tags:
- secrets
- fear
- character
- attitude
- truth
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Mar-2012c)
CREATE (t:THOUGHT {
    name: "thought.TERRIBLE SECRETS",
    alias: "Thought: Terrible Secrets",
    parent: "topic.ATTITUDE",
    tags: ['secrets', 'fear', 'character', 'attitude', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TERRIBLE SECRETS",
    en_title: "Terrible Secrets",
    en_content: "Secrets can be terrible things.",
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
WHERE t.name = "thought.TERRIBLE SECRETS" AND c.name = "content.TERRIBLE SECRETS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TERRIBLE SECRETS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.TERRIBLE SECRETS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >TERRIBLE SECRETS" }]->(child);
```
