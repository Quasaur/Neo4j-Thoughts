---
name: "thought.IMAGE OF GOD"
alias: "Thought: Image Of God"
type: THOUGHT
parent: "topic.CREATION"
tags:
- creation
- identity
- image
- god
- value
level: 2
neo4j: true
insert: true
---
# Image Of God

> [!Thought-en]
> I'm NOT the child of monkeys; I was created in God's Image and after His Likeness; I should be treated as such--and so should you!

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012c_2)
CREATE (t:THOUGHT {
    name: "thought.IMAGE OF GOD",
    alias: "Thought: Image Of God",
    parent: "topic.CREATION",
    tags: ['creation', 'identity', 'image', 'god', 'value'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMAGE OF GOD",
    en_title: "Image Of God",
    en_content: "I'm NOT the child of monkeys; I was created in God's Image and after His Likeness; I should be treated as such--and so should you!",
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
WHERE t.name = "thought.IMAGE OF GOD" AND c.name = "content.IMAGE OF GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.IMAGE OF GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.IMAGE OF GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >IMAGE OF GOD" }]->(child);
```