---
name: "thought.DEFINING EVIL PRIDE"
alias: "Thought: Defining Evil Pride"
type: THOUGHT
parent: "topic.EVIL"
tags:
- evil
- pride
- self
- treasure
- character
level: 2
neo4j: true
insert: true
---
# Defining Evil Pride

> [!Thought-en]
> Evil is considering this God-given treasure (Self) more precious than The God Who gave it.

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.DEFINING EVIL PRIDE",
    alias: "Thought: Defining Evil Pride",
    parent: "topic.EVIL",
    tags: ['evil', 'pride', 'self', 'treasure', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEFINING EVIL PRIDE",
    en_title: "Defining Evil Pride",
    en_content: "Evil is considering this God-given treasure (Self) more precious than The God Who gave it.",
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
WHERE t.name = "thought.DEFINING EVIL PRIDE" AND c.name = "content.DEFINING EVIL PRIDE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINING EVIL PRIDE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DEFINING EVIL PRIDE"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >DEFINING EVIL PRIDE" }]->(child);
```