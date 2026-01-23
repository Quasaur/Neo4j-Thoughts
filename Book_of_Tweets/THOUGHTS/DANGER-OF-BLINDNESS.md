---
name: "thought.DANGER OF BLINDNESS"
alias: "Thought: Danger Of Blindness"
type: THOUGHT
en_content: "Blindness is great...until you fall off a cliff."
parent: "topic.UNDERSTANDING"
tags:
- blindness
- danger
- wisdom
- discernment
- truth
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 13-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.DANGER OF BLINDNESS",
    alias: "Thought: Danger Of Blindness",
    parent: "topic.UNDERSTANDING",
    tags: ['blindness', 'danger', 'wisdom', 'discernment', 'truth'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DANGER OF BLINDNESS",
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

MATCH (t:THOUGHT {name: "thought.DANGER OF BLINDNESS"})
MATCH (c:CONTENT {name: "content.DANGER OF BLINDNESS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DANGER OF BLINDNESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.UNDERSTANDING"})
MATCH (child:THOUGHT {name: "thought.DANGER OF BLINDNESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "UNDERSTANDING >DANGER OF BLINDNESS" }]->(child);
```
