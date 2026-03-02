---
type: THOUGHT
name: "thought.HUMANITARIANISM"
alias: "Thought: HUMANITARIANISM"
parent: "topic.RELIGION"
tags: ["humanity", "self_worship", "god", "judgment", "accountable"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMANITARIANISM",
    alias: "Thought: HUMANITARIANISM",
    parent: "topic.RELIGION",
    tags: ["humanity", "self_worship", "god", "judgment", "accountable"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMANITARIANISM",
    ctype: "THOUGHT",
    en_title: "HUMANITARIANISM",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMANITARIANISM" AND c.name = "content.HUMANITARIANISM"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMANITARIANISM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.HUMANITARIANISM"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->HUMANITARIANISM"}]->(child);
```