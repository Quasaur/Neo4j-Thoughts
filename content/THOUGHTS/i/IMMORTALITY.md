---
name: thought.IMMORTALITY
alias: "Thought: IMMORTALITY"
type: THOUGHT
parent: topic.FAITHFULNESS
tags:
- immortality
- eternallife
- salvation
- desire
- jesuschrist
neo4j: true
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IMMORTALITY",
    alias: "Thought: IMMORTALITY",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternallife", "salvation", "desire", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IMMORTALITY",
    en_title: "IMMORTALITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IMMORTALITY" AND c.name = "content.IMMORTALITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.IMMORTALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.IMMORTALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITHFULNESS->IMMORTALITY"}]->(child);
```