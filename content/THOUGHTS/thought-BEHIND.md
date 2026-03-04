---
type: THOUGHT
name: "thought.BEHIND"
alias: "Thought: Behind"
parent: "topic.DIVINE-SOVEREIGNTY"
tags: ["divine", "sovereignty", "impetus", "control", "all"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BEHIND",
    alias: "Thought: Behind",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["divine", "sovereignty", "impetus", "control", "all"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.BEHIND",
    ctype: "THOUGHT",
    en_title: "Behind",
 es_title: "DETRÁS",
 fr_title: "DERRIÈRE",
 hi_title: "पीछे",
 zh_title: "zài hòu miàn",
    en_content: "",
 es_content: "Dios está detrás de todo",
 fr_content: "Dieu est derrière tout",
 hi_content: "हर चीज़ के पीछे भगवान है",
 zh_content: "shén shì yī qiè de bèi hòu"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BEHIND" AND c.name = "content.BEHIND"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.BEHIND"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.BEHIND"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->BEHIND"}]->(child);
```