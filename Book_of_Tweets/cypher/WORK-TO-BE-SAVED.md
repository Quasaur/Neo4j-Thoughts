---
name: "thought.WORK TO BE SAVED"
alias: "Thought: Work To Be Saved"
type: THOUGHT
en_content: "Getting saved is hard work; but hard work alone won't get you saved."
parent: "topic.GRACE"
tags:
- salvation
- work
- grace
- effort
- power
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.WORK TO BE SAVED",
    alias: "Thought: Work To Be Saved",
    parent: "topic.GRACE",
    tags: ['salvation', 'work', 'grace', 'effort', 'power'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WORK TO BE SAVED",
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

MATCH (t:THOUGHT {name: "thought.WORK TO BE SAVED"})
MATCH (c:CONTENT {name: "content.WORK TO BE SAVED"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.WORK TO BE SAVED" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.WORK TO BE SAVED"})
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >WORK TO BE SAVED" }]->(child);
```
