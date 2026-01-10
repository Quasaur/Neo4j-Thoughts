---
name: "thought.NATION FORGETTING GOD"
alias: "Thought: Nation Forgetting God"
type: THOUGHT
en_content: "I'm watching a nation that has forgotten God turn into Hell."
parent: "topic.MORALITY"
tags:
- nation
- hell
- god
- morality
- judgment
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.NATION FORGETTING GOD",
    alias: "Thought: Nation Forgetting God",
    parent: "topic.MORALITY",
    tags: ['nation', 'hell', 'god', 'morality', 'judgment'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NATION FORGETTING GOD",
    en_title: "Nation Forgetting God",
    en_content: "I'm watching a nation that has forgotten God turn into Hell.",
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
WHERE t.name = "thought.NATION FORGETTING GOD" AND c.name = "content.NATION FORGETTING GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATION FORGETTING GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.NATION FORGETTING GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >NATION FORGETTING GOD" }]->(child);
```
