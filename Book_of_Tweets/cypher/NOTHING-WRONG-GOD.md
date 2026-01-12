---
name: "thought.NOTHING WRONG GOD"
alias: "Thought: Nothing Wrong God"
type: THOUGHT
en_content: "There is nothing wrong with God."
parent: "topic.THE GODHEAD"
tags:
- character
- perfection
- god
- divinity
- truth
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-Feb-2013)
CREATE (t:THOUGHT {
    name: "thought.NOTHING WRONG GOD",
    alias: "Thought: Nothing Wrong God",
    parent: "topic.THE GODHEAD",
    tags: ['character', 'perfection', 'god', 'divinity', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NOTHING WRONG GOD",
    en_title: "Nothing Wrong God",
    en_content: "There is nothing wrong with God.",
    es_title: "Nada Malo en Dios",
    es_content: "No hay nada malo en Dios.",
    fr_title: "Rien de Mal en Dieu",
    fr_content: "Il n'y a rien de mal en Dieu.",
    hi_title: "परमेश्वर में कोई दोष नहीं",
    hi_content: "परमेश्वर में कोई दोष नहीं है।",
    zh_title: "Shén méiyǒu cuòwù",
    zh_content: "Shén méiyǒu rènhé cuòwù."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOTHING WRONG GOD" AND c.name = "content.NOTHING WRONG GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOTHING WRONG GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NOTHING WRONG GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NOTHING WRONG GOD" }]->(child);
```
