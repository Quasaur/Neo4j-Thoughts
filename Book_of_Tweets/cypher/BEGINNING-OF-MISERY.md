---
name: "thought.BEGINNING OF MISERY"
alias: "Thought: Beginning Of Misery"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- misery
- pride
- humanity
- origin
- god
level: 3
neo4j: true
insert: true
---
# Beginning Of Misery

> [!Thought-en]
> Misery began when some idiot decided he was more important than God.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.BEGINNING OF MISERY",
    alias: "Thought: Beginning Of Misery",
    parent: "topic.HUMANITY",
    tags: ['misery', 'pride', 'humanity', 'origin', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BEGINNING OF MISERY",
    en_title: "Beginning Of Misery",
    en_content: "Misery began when some idiot decided he was more important than God.",
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
WHERE t.name = "thought.BEGINNING OF MISERY" AND c.name = "content.BEGINNING OF MISERY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BEGINNING OF MISERY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.BEGINNING OF MISERY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >BEGINNING OF MISERY" }]->(child);
```