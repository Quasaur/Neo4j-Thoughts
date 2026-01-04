---
name: "thought.SAYING NO TO SELF"
alias: "Thought: Saying No To Self"
type: THOUGHT
en_content: "Only a person who can say no to themselves can say no to the world and to the devil."
parent: "topic.SPIRITUALITY"
tags:
- discipline
- self_denial
- world
- devil
- character
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Oct-2012c)
CREATE (t:THOUGHT {
    name: "thought.SAYING NO TO SELF",
    alias: "Thought: Saying No To Self",
    parent: "topic.SPIRITUALITY",
    tags: ['discipline', 'self_denial', 'world', 'devil', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SAYING NO TO SELF",
    en_title: "Saying No To Self",
    en_content: "Only a person who can say no to themselves can say no to the world and to the devil.",
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
WHERE t.name = "thought.SAYING NO TO SELF" AND c.name = "content.SAYING NO TO SELF"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAYING NO TO SELF" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SAYING NO TO SELF"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SAYING NO TO SELF" }]->(child);
```
