---
type: THOUGHT
name: "thought.WORK TO BE SAVED"
alias: "Thought: Work To Be Saved"
parent: "topic.GRACE"
en_content: "Getting saved is hard work; but hard work alone won't get you saved."
tags: ["salvation", "work", "grace", "effort", "power"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WORK TO BE SAVED",
    alias: "Thought: Work To Be Saved",
    parent: "topic.GRACE",
    tags: ['salvation', 'work', 'grace', 'effort', 'power'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WORK TO BE SAVED",
    ctype: "THOUGHT",
    en_title: "Work To Be Saved",
    en_content: "Getting saved is hard work; but hard work alone won't get you saved.",
    es_title: "Trabajar Para Ser Salvado",
    es_content: "Ser salvado requiere trabajo duro; pero el trabajo duro por sí solo no te salvará.",
    fr_title: "Travailler Pour Être Sauvé",
    fr_content: "Être sauvé demande un travail acharné ; mais le travail acharné seul ne vous sauvera pas.",
    hi_title: "मुक्ति पाने के लिए कार्य",
    hi_content: "मुक्ति पाना कठिन परिश्रम है; परन्तु केवल कठिन परिश्रम से मुक्ति नहीं मिलेगी।",
    zh_title: "Wei De Jiu En Er Gong Zuo",
    zh_content: "De jiu en shi jian nan de gong zuo; dan jin jin kao jian nan de gong zuo bu neng shi ni de jiu."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WORK TO BE SAVED"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->WORK TO BE SAVED"
RETURN t, parent;
```
