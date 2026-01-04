---
name: "thought.BAG OF CHEMICALS DUPED"
alias: "Thought: Bag Of Chemicals Duped"
type: THOUGHT
parent: "topic.HUMANITY"
tags:
- humanity
- chemistry
- deception
- spirit
- science
level: 3
neo4j: true
insert: true
---
# Bag Of Chemicals Duped

> [!Thought-en]
> It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity.

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Aug-2013c)
CREATE (t:THOUGHT {
    name: "thought.BAG OF CHEMICALS DUPED",
    alias: "Thought: Bag Of Chemicals Duped",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'chemistry', 'deception', 'spirit', 'science'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BAG OF CHEMICALS DUPED",
    en_title: "Bag Of Chemicals Duped",
    en_content: "It's hard to fathom that people can be duped into thinking they're nothing more than a bag of chemicals and electricity.",
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
WHERE t.name = "thought.BAG OF CHEMICALS DUPED" AND c.name = "content.BAG OF CHEMICALS DUPED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BAG OF CHEMICALS DUPED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.BAG OF CHEMICALS DUPED"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >BAG OF CHEMICALS DUPED" }]->(child);
```