---
name: thought.HUMAN_MERCY
alias: "Thought: HUMAN MERCY"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- mercy
- submission
- faithfulness
- obedience
- jesuschrist
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN_MERCY",
    alias: "Thought: HUMAN MERCY",
    parent: "topic.ATTITUDE",
    tags: ["mercy", "submission", "faithfulness", "obedience", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN_MERCY",
    en_title: "HUMAN MERCY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN_MERCY" AND c.name = "content.HUMAN_MERCY"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN_MERCY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HUMAN_MERCY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->HUMAN_MERCY"}]->(child);
```