---
name: "thought.CAT ON KNEE"
alias: "Thought: Cat On Knee"
type: THOUGHT
en_content: "My cat will jump up on my knee, and from there knock things off the table so he can play with them on the floor...God is great!"
parent: "topic.CREATION"
tags:
- creation
- nature
- design
- cat
- humor
level: 2
neo4j: true
insert: true
---
# Cat On Knee

> [!Thought-en]
> My cat will jump up on my knee, and from there knock things off the table so he can play with them on the floor...God is great!

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.CAT ON KNEE",
    alias: "Thought: Cat On Knee",
    parent: "topic.CREATION",
    tags: ['creation', 'nature', 'design', 'cat', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.CAT ON KNEE",
    en_title: "Cat On Knee",
    en_content: "My cat will jump up on my knee, and from there knock things off the table so he can play with them on the floor...God is great!",
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
WHERE t.name = "thought.CAT ON KNEE" AND c.name = "content.CAT ON KNEE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CAT ON KNEE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.CAT ON KNEE"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >CAT ON KNEE" }]->(child);
```