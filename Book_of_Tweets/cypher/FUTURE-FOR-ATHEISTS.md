---
name: "thought.FUTURE FOR ATHEISTS"
alias: "Thought: Future For Atheists"
type: THOUGHT
parent: "topic.PHILOSOPHY"
tags:
- future
- creator
- atheism
- philosophy
level: 4
neo4j: true
insert: true
---
# Future For Atheists

> [!Thought-en]
> Is there any future for a species that so despises its Creator as to announce that He doesn't exist?

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.FUTURE FOR ATHEISTS",
    alias: "Thought: Future For Atheists",
    parent: "topic.PHILOSOPHY",
    tags: ['future', 'creator', 'atheism', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FUTURE FOR ATHEISTS",
    en_title: "Future For Atheists",
    en_content: "Is there any future for a species that so despises its Creator as to announce that He doesn't exist?",
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
WHERE t.name = "thought.FUTURE FOR ATHEISTS" AND c.name = "content.FUTURE FOR ATHEISTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FUTURE FOR ATHEISTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.FUTURE FOR ATHEISTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >FUTURE FOR ATHEISTS" }]->(child);
```