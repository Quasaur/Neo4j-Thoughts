---
name: thought.NEAR_TO_GOD
alias: "Thought: NEAR TO GOD"
type: THOUGHT
parent: topic.EVIL
tags:
- access
- calling
- desire
- predestined
- foreknowledge
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NEAR_TO_GOD",
    alias: "Thought: NEAR TO GOD",
    parent: "topic.EVIL",
    tags: ["access", "calling", "desire", "predestined", "foreknowledge"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NEAR_TO_GOD",
    en_title: "NEAR TO GOD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NEAR_TO_GOD" AND c.name = "content.NEAR_TO_GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.NEAR_TO_GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.NEAR_TO_GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->NEAR_TO_GOD"}]->(child);
```