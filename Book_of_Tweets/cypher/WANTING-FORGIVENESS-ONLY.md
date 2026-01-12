---
name: "thought.WANTING FORGIVENESS ONLY"
alias: "Thought: Wanting Forgiveness Only"
type: THOUGHT
en_content: "We want to be forgiven, but we don't want to forgive...how disgusting."
parent: "topic.ATTITUDE"
tags:
- forgiveness
- hypocrisy
- attitude
- character
- disgusting
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.WANTING FORGIVENESS ONLY",
    alias: "Thought: Wanting Forgiveness Only",
    parent: "topic.ATTITUDE",
    tags: ['forgiveness', 'hypocrisy', 'attitude', 'character', 'disgusting'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WANTING FORGIVENESS ONLY",
    en_title: "Wanting Forgiveness Only",
    en_content: "We want to be forgiven, but we don't want to forgive...how disgusting.",
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
WHERE t.name = "thought.WANTING FORGIVENESS ONLY" AND c.name = "content.WANTING FORGIVENESS ONLY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WANTING FORGIVENESS ONLY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.WANTING FORGIVENESS ONLY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >WANTING FORGIVENESS ONLY" }]->(child);
```
