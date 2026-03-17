---
type: THOUGHT
name: "thought.NOT LOOKING IDIOT"
alias: "Thought: Not Looking Like an Idiot"
parent: "topic.ATTITUDE"
en_content: "I don't mind being an idiot, just looking like one."
tags: ["idiot", "appearance", "attitude", "character"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NOT LOOKING IDIOT",
    alias: "Thought: Not Looking Like an Idiot",
    parent: "topic.ATTITUDE",
    tags: ['idiot', 'appearance', 'attitude', 'character'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOT LOOKING IDIOT",
    ctype: "THOUGHT",
    en_title: "Not Looking Idiot",
    en_content: "I don't mind being an idiot, just looking like one.",
    es_title: "No Parecer Idiota",
    es_content: "No me importa ser un idiota, solo parecerlo.",
    fr_title: "Ne Pas Avoir l'Air Idiot",
    fr_content: "Cela ne me dérange pas d'être un idiot, juste d'en avoir l'air.",
    hi_title: "मूर्ख न दिखना",
    hi_content: "मुझे मूर्ख होने से कोई परेशानी नहीं है, बस मूर्ख दिखने से है।",
    zh_title: "Bu Xiang Kan Qi Lai Xiang Sha Gua",
    zh_content: "Wo Bu Jie Yi Dang Sha Gua, Zhi Shi Bu Xiang Kan Qi Lai Xiang Sha Gua."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOT LOOKING IDIOT"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->NOT LOOKING IDIOT"
RETURN t, parent;
```
