---
type: THOUGHT
name: "thought.FICTIONAL CHARACTERS"
alias: "Thought: Fictional Characters"
parent: "topic.THE GODHEAD"
en_content: "Compared to GOD we are all fictional characters."
tags: ["god", "creation", "reality", "majesty", "transcendence"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-May-2011a)
CREATE (t:THOUGHT {    name: "thought.FICTIONAL CHARACTERS",
    alias: "Thought: Fictional Characters",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'creation', 'reality', 'majesty', 'transcendence'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.FICTIONAL CHARACTERS",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FICTIONAL CHARACTERS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->FICTIONAL CHARACTERS"
RETURN t, parent;
```
