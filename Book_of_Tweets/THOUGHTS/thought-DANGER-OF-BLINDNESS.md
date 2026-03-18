---
type: THOUGHT
name: "thought.DANGER OF BLINDNESS"
alias: "Thought: Danger Of Blindness"
parent: "topic.UNDERSTANDING"
en_content: "Blindness is great...until you fall off a cliff."
tags: ["blindness", "danger", "wisdom", "discernment", "truth"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Oct-2010)
CREATE (t:THOUGHT {    name: "thought.DANGER OF BLINDNESS",
    alias: "Thought: Danger Of Blindness",
    parent: "topic.UNDERSTANDING",
    tags: ['blindness', 'danger', 'wisdom', 'discernment', 'truth'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DANGER OF BLINDNESS",
    ctype: "THOUGHT",
    en_title: "Danger Of Blindness",
    en_content: "Blindness is great...until you fall off a cliff.",
    es_title: "Peligro de la Ceguera",
    es_content: "La ceguera es genial... hasta que caes de un acantilado.",
    fr_title: "Danger de la Cécité",
    fr_content: "La cécité est formidable... jusqu'à ce que vous tombiez d'une falaise.",
    hi_title: "अंधेपन का खतरा",
    hi_content: "अंधापन बहुत अच्छा है... जब तक आप एक चट्टान से नहीं गिर जाते।",
    zh_title: "Xiāyǎn de Wéixiǎn",
    zh_content: "Xiāyǎn hěn bàng... Zhídào nǐ cóng xuányá shàng diào xiàlái."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DANGER OF BLINDNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.UNDERSTANDING->DANGER OF BLINDNESS"
RETURN t, parent;
```
