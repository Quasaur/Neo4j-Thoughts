---
name: "thought.SIN IS EXPENSIVE"
alias: "Thought: Sin Is Expensive"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- sin
- cost
- society
- morality
- consequences
level: 3
neo4j: true
insert: true
---
# Sin Is Expensive

> [!Thought-en]
> Law enforcement, court costs incarceration, healthcare, security, protection, insurance premiums, funeral costs...Sin is expensive!

```Cypher
// Generated from Book6E-FINAL.md (ID: 02-Nov-2013a)
CREATE (t:THOUGHT {
    name: "thought.SIN IS EXPENSIVE",
    alias: "Thought: Sin Is Expensive",
    parent: "topic.MORALITY",
    tags: ['sin', 'cost', 'society', 'morality', 'consequences'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SIN IS EXPENSIVE",
    en_title: "Sin Is Expensive",
    en_content: "Law enforcement, court costs incarceration, healthcare, security, protection, insurance premiums, funeral costs...Sin is expensive!",
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
WHERE t.name = "thought.SIN IS EXPENSIVE" AND c.name = "content.SIN IS EXPENSIVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SIN IS EXPENSIVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SIN IS EXPENSIVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SIN IS EXPENSIVE" }]->(child);
```