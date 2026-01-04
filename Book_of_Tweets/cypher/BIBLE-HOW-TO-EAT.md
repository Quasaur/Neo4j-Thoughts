---
name: "thought.BIBLE HOW TO EAT"
alias: "Thought: Bible How To Eat"
type: THOUGHT
en_content: "The Bible not only tells us how to live, but also HOW TO EAT!"
parent: "topic.TRUTH"
tags:
- bible
- food
- health
- truth
- life
level: 2
neo4j: true
insert: true
---
# Bible How To Eat

> [!Thought-en]
> The Bible not only tells us how to live, but also HOW TO EAT!

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013f)
CREATE (t:THOUGHT {
    name: "thought.BIBLE HOW TO EAT",
    alias: "Thought: Bible How To Eat",
    parent: "topic.TRUTH",
    tags: ['bible', 'food', 'health', 'truth', 'life'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BIBLE HOW TO EAT",
    en_title: "Bible How To Eat",
    en_content: "The Bible not only tells us how to live, but also HOW TO EAT!",
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
WHERE t.name = "thought.BIBLE HOW TO EAT" AND c.name = "content.BIBLE HOW TO EAT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BIBLE HOW TO EAT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.BIBLE HOW TO EAT"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >BIBLE HOW TO EAT" }]->(child);
```