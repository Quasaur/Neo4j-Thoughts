---
name: "thought.GODS FORGETFULNESS"
alias: "Thought: Gods Forgetfulness"
type: THOUGHT
en_content: "Don't bring to mind what God has decided to forget."
parent: "topic.GRACE"
tags:
- forgiveness
- memory
- grace
- peace
- character
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Feb-2012b)
CREATE (t:THOUGHT {
    name: "thought.GODS FORGETFULNESS",
    alias: "Thought: Gods Forgetfulness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'memory', 'grace', 'peace', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GODS FORGETFULNESS",
    en_title: "Gods Forgetfulness",
    en_content: "Don't bring to mind what God has decided to forget.",
    es_title: "El Olvido de Dios",
    es_content: "No traigas a la mente lo que Dios ha decidido olvidar.",
    fr_title: "L'Oubli de Dieu",
    fr_content: "Ne rappelle pas à l'esprit ce que Dieu a décidé d'oublier.",
    hi_title: "परमेश्वर की विस्मृति",
    hi_content: "जिसे परमेश्वर ने भुलाने का निर्णय लिया है, उसे मन में न लाएं।",
    zh_title: "Shén de Yíwàng",
    zh_content: "Bùyào tí qǐ Shàngdì juédìng yíwàng de shìqíng."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS FORGETFULNESS" AND c.name = "content.GODS FORGETFULNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GODS FORGETFULNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GODS FORGETFULNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >GODS FORGETFULNESS" }]->(child);
```
