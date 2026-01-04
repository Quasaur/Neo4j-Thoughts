---
name: "thought.GRACE TO HUMBLE"
alias: "Thought: Grace To Humble"
type: THOUGHT
en_content: "Salvation in a Nutshell: God resists the proud, but gives Grace to the humble."
parent: "topic.GRACE"
tags:
- grace
- humility
- proud
- god
- salvation
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Jan-2012b)
CREATE (t:THOUGHT {
    name: "thought.GRACE TO HUMBLE",
    alias: "Thought: Grace To Humble",
    parent: "topic.GRACE",
    tags: ['grace', 'humility', 'proud', 'god', 'salvation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GRACE TO HUMBLE",
    en_title: "Grace To Humble",
    en_content: "Salvation in a Nutshell: God resists the proud, but gives Grace to the humble.",
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
WHERE t.name = "thought.GRACE TO HUMBLE" AND c.name = "content.GRACE TO HUMBLE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GRACE TO HUMBLE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GRACE TO HUMBLE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GRACE TO HUMBLE" }]->(child);
```
