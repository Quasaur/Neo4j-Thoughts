---
name: thought.DIVINE_SEED
alias: "Thought: DIVINE SEED"
type: THOUGHT
parent: topic.GRACE
tags:
- seed
- wordofgod
- holyspirit
- sowing
- reaping
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIVINE_SEED",
    alias: "Thought: DIVINE SEED",
    parent: "topic.GRACE",
    tags: ["seed", "wordofgod", "holyspirit", "sowing", "reaping"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIVINE_SEED",
    en_title: "DIVINE SEED",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIVINE_SEED" AND c.name = "content.DIVINE_SEED"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE_SEED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DIVINE_SEED"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->DIVINE_SEED"}]->(child);
```