---
name: "thought.FICTIONAL CHARACTERS"
alias: "Thought: Fictional Characters"
type: THOUGHT
parent: "topic.THE GODHEAD"
tags:
- god
- creation
- reality
- majesty
- transcendence
level: 1
neo4j: true
insert: true
---
# Fictional Characters

> [!Thought-en]
> Compared to GOD we are all fictional characters.

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-May-2011a)
CREATE (t:THOUGHT {
    name: "thought.FICTIONAL CHARACTERS",
    alias: "Thought: Fictional Characters",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'creation', 'reality', 'majesty', 'transcendence'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.FICTIONAL CHARACTERS",
    en_title: "Fictional Characters",
    en_content: "Compared to GOD we are all fictional characters.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FICTIONAL CHARACTERS" AND c.name = "content.FICTIONAL CHARACTERS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FICTIONAL CHARACTERS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.FICTIONAL CHARACTERS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >FICTIONAL CHARACTERS" }]->(child);
```