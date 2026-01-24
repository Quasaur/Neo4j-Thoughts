---
name: thought.HUMANITARIANISM
alias: "Thought: HUMANITARIANISM"
type: THOUGHT
parent: topic.RELIGION
tags:
- humanity
- selfworship
- god
- judgment
- accountable
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMANITARIANISM",
    alias: "Thought: HUMANITARIANISM",
    parent: "topic.RELIGION",
    tags: ["humanity", "selfworship", "god", "judgment", "accountable"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMANITARIANISM",
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