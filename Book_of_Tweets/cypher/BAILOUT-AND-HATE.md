---
name: "thought.BAILOUT AND HATE"
alias: "Thought: Bailout And Hate"
type: THOUGHT
en_content: "Obama bailed out the Republicans...which made them hate him all the more."
parent: "topic.MORALITY"
tags:
- politics
- gratitude
- hate
- morality
- society
level: 3
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.BAILOUT AND HATE",
    alias: "Thought: Bailout And Hate",
    parent: "topic.MORALITY",
    tags: ['politics', 'gratitude', 'hate', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BAILOUT AND HATE",
    en_title: "Bailout And Hate",
    en_content: "Obama bailed out the Republicans...which made them hate him all the more.",
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
WHERE t.name = "thought.BAILOUT AND HATE" AND c.name = "content.BAILOUT AND HATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BAILOUT AND HATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.BAILOUT AND HATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >BAILOUT AND HATE" }]->(child);
```
