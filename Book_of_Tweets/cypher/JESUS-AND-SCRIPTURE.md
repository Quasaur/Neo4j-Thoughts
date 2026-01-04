---
name: "thought.JESUS AND SCRIPTURE"
alias: "Thought: Jesus And Scripture"
type: THOUGHT
parent: "topic.TRUTH"
tags:
- jesus
- scripture
- bible
- truth
- testimony
level: 2
neo4j: true
insert: true
---
# Jesus And Scripture

> [!Thought-en]
> Jesus treated the Scriptures as the Testimony of God...I would be foolish to do otherwise.

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.JESUS AND SCRIPTURE",
    alias: "Thought: Jesus And Scripture",
    parent: "topic.TRUTH",
    tags: ['jesus', 'scripture', 'bible', 'truth', 'testimony'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.JESUS AND SCRIPTURE",
    en_title: "Jesus And Scripture",
    en_content: "Jesus treated the Scriptures as the Testimony of God...I would be foolish to do otherwise.",
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
WHERE t.name = "thought.JESUS AND SCRIPTURE" AND c.name = "content.JESUS AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.JESUS AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.JESUS AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >JESUS AND SCRIPTURE" }]->(child);
```