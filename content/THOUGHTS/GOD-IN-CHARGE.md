---
name: thought.GOD_IN_CHARGE
alias: "Thought: GOD IN CHARGE"
type: THOUGHT
parent: topic.DIVINE-SOVEREIGNTY
tags:
- belief
- truth
- control
- god
- sovereignty
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GOD_IN_CHARGE",
    alias: "Thought: GOD IN CHARGE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["belief", "truth", "control", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD_IN_CHARGE",
    en_title: "GOD IN CHARGE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD_IN_CHARGE" AND c.name = "content.GOD_IN_CHARGE"
MERGE (t)-[:HAS_CONTENT {name: "edge.GOD_IN_CHARGE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.GOD_IN_CHARGE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->GOD_IN_CHARGE"}]->(child);
```