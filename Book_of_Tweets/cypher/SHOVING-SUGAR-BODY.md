---
name: "thought.SHOVING SUGAR BODY"
alias: "Thought: Shoving Sugar Body"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- sugar
- health
- body
- diabetes
- morality
level: 3
neo4j: true
insert: true
---
# Shoving Sugar Body

> [!Thought-en]
> We keep shoving sugar into a body that itself manufactures sugar and then wonder why we get diabetes!

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013b)
CREATE (t:THOUGHT {
    name: "thought.SHOVING SUGAR BODY",
    alias: "Thought: Shoving Sugar Body",
    parent: "topic.MORALITY",
    tags: ['sugar', 'health', 'body', 'diabetes', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOVING SUGAR BODY",
    en_title: "Shoving Sugar Body",
    en_content: "We keep shoving sugar into a body that itself manufactures sugar and then wonder why we get diabetes!",
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
WHERE t.name = "thought.SHOVING SUGAR BODY" AND c.name = "content.SHOVING SUGAR BODY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SHOVING SUGAR BODY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SHOVING SUGAR BODY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >SHOVING SUGAR BODY" }]->(child);
```