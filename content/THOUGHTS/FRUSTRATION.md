---
name: thought.FRUSTRATION
alias: "Thought: FRUSTRATION"
type: THOUGHT
parent: topic.FAITHFULNESS
tags:
- frustration
- spirituality
- assurance
- fathergod
- jesuschrist
neo4j: true
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FRUSTRATION",
    alias: "Thought: FRUSTRATION",
    parent: "topic.FAITHFULNESS",
    tags: ["frustration", "spirituality", "assurance", "fathergod", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FRUSTRATION",
    en_title: "FRUSTRATION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FRUSTRATION" AND c.name = "content.FRUSTRATION"
MERGE (t)-[:HAS_CONTENT {name: "edge.FRUSTRATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.FRUSTRATION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITHFULNESS->FRUSTRATION"}]->(child);
```