---
type: THOUGHT
name: "thought.ELECTROMAGNETISM TOUCH"
alias: "Thought: Electromagnetism Touch"
parent: "topic.PHYSICS"
en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!"
tags: ["science", "physics", "creation", "design", "power"]
ptopic: "[[topic-PHYSICS]]"
level: 6
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ELECTROMAGNETISM TOUCH",
    alias: "Thought: Electromagnetism Touch",
    parent: "topic.PHYSICS",
    tags: ['science', 'physics', 'creation', 'design', 'power'],
    level: 6
});

CREATE (c:CONTENT {
    name: "content.ELECTROMAGNETISM TOUCH",
    ctype: "THOUGHT",
    en_title: "Electromagnetism Touch",
    en_content: "Under normal circumstances, electromagnetism prevents any 2 surfaces from touching...God is great!",
    es_title: "Toque Electromagnético",
    es_content: "En circunstancias normales, el electromagnetismo impide que cualquier 2 superficies se toquen...¡Dios es grande!",
    fr_title: "Toucher Électromagnétique",
    fr_content: "Dans des circonstances normales, l'électromagnétisme empêche 2 surfaces de se toucher...Dieu est grand !",
    hi_title: "विद्युत चुम्बकीय स्पर्श",
    hi_content: "सामान्य परिस्थितियों में, विद्युत चुम्बकत्व किसी भी 2 सतहों को छूने से रोकता है...परमेश्वर महान है!",
    zh_title: "Dianci Chumo",
    zh_content: "Zai zhengchang qingkuang xia, dianci zu zhi renhe liang ge biaomian xiangchu...Shangdi shi weida de!"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ELECTROMAGNETISM TOUCH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHYSICS"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHYSICS->ELECTROMAGNETISM TOUCH"
RETURN t, parent;
```
