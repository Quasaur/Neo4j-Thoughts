---
name: thought.CITIZENSHIP
alias: "Thought: CITIZENSHIP"
type: THOUGHT
parent: topic.ECONOMICS
tags:
- citizenship
- kingdom
- reignofgod
- freedom
- jesuschrist
neo4j: true
ptopic: "[[topic-ECONOMICS]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.CITIZENSHIP",
    alias: "Thought: CITIZENSHIP",
    parent: "topic.ECONOMICS",
    tags: ["citizenship", "kingdom", "reignofgod", "freedom", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CITIZENSHIP",
    en_title: "CITIZENSHIP",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CITIZENSHIP" AND c.name = "content.CITIZENSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.CITIZENSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ECONOMICS" AND child.name = "thought.CITIZENSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ECONOMICS->CITIZENSHIP"}]->(child);
```