---
type: THOUGHT
name: "thought.IDIOTS ALL"
alias: "Thought: Idiots All"
parent: "topic.PSYCHOLOGY"
en_content: "Everyone's an idiot about something!"
tags: ["foolish", "stupid", "humanity", "everyone", "intelligence"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.IDIOTS ALL",
    alias: "Thought: Idiots All",
    parent: "topic.PSYCHOLOGY",
    tags: ["foolish", "stupid", "humanity", "everyone", "intelligence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.IDIOTS ALL",
    ctype: "THOUGHT",
    en_title: "Idiots All",
    en_content: "Everyone's an idiot about something!",
    es_title: "IDIOTAS TODOS",
    es_content: "¡Todo el mundo es idiota por algo!",
    fr_title: "LES IDIOTS TOUS",
    fr_content: "Tout le monde est idiot à propos de quelque chose !",
    hi_title: "सभी बेवकूफ",
    hi_content: "हर कोई किसी न किसी मामले में मूर्ख है!",
    zh_title: "dōu shì bái chī",
    zh_content: "měi gè rén zài mǒu xiē shì qíng shàng dōu shì bái chī ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.IDIOTS ALL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->IDIOTS ALL"
RETURN t, parent;
```
