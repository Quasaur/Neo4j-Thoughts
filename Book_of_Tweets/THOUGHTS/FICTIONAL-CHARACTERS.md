---
name: "thought.FICTIONAL CHARACTERS"
alias: "Thought: Fictional Characters"
type: THOUGHT
en_content: "Compared to GOD we are all fictional characters."
parent: "topic.THE GODHEAD"
tags:
- god
- creation
- reality
- majesty
- transcendence
level: 1
neo4j: false
ptopic: 
---

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
    es_title: "Personajes Ficticios",
    es_content: "Comparados con DIOS todos somos personajes ficticios.",
    fr_title: "Personnages Fictifs",
    fr_content: "Comparés à DIEU nous sommes tous des personnages fictifs.",
    hi_title: "काल्पनिक पात्र",
    hi_content: "परमेश्वर की तुलना में हम सभी काल्पनिक पात्र हैं।",
    zh_title: "Xūgòu Rénwù",
    zh_content: "Yǔ SHÀNGDÌ xiāngbǐ, wǒmen dōu shì xūgòu rénwù."
});

MATCH (t:THOUGHT {name: "thought.FICTIONAL CHARACTERS"})
MATCH (c:CONTENT {name: "content.FICTIONAL CHARACTERS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FICTIONAL CHARACTERS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.FICTIONAL CHARACTERS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->FICTIONAL CHARACTERS" }]->(child);
```
