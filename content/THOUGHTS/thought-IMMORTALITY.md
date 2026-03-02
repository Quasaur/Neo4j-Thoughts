---
type: THOUGHT
name: "thought.IMMORTALITY"
alias: "Thought: IMMORTALITY"
parent: "topic.FAITHFULNESS"
tags: ["immortality", "eternal_life", "salvation", "desire", "jesus_christ"]
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.IMMORTALITY",
    alias: "Thought: IMMORTALITY",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternal_life", "salvation", "desire", "jesus_christ"],
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
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITHFULNESS->IMMORTALITY"}]->(child);
```