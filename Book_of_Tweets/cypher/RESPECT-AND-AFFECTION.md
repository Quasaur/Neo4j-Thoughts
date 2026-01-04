---
name: "thought.RESPECT AND AFFECTION"
alias: "Thought: Respect And Affection"
type: THOUGHT
en_content: "Respect breeds affection."
parent: "topic.MORALITY"
tags:
- respect
- affection
- relationship
- morality
- character
level: 3
neo4j: true
insert: true
---
# Respect And Affection

> [!Thought-en]
> Respect breeds affection.

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.RESPECT AND AFFECTION",
    alias: "Thought: Respect And Affection",
    parent: "topic.MORALITY",
    tags: ['respect', 'affection', 'relationship', 'morality', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RESPECT AND AFFECTION",
    en_title: "Respect And Affection",
    en_content: "Respect breeds affection.",
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
WHERE t.name = "thought.RESPECT AND AFFECTION" AND c.name = "content.RESPECT AND AFFECTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.RESPECT AND AFFECTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.RESPECT AND AFFECTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >RESPECT AND AFFECTION" }]->(child);
```