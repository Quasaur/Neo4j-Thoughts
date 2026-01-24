---
name: thought.SHOULD
alias: "Thought: SHOULD"
type: THOUGHT
parent: topic.MORALITY
tags:
- law
- order
- discipline
- principle
- god
neo4j: true
ptopic: "[[topic-MORALITY]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SHOULD",
    alias: "Thought: SHOULD",
    parent: "topic.MORALITY",
    tags: ["law", "order", "discipline", "principle", "god"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOULD",
    en_title: "SHOULD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHOULD" AND c.name = "content.SHOULD"
MERGE (t)-[:HAS_CONTENT {name: "edge.SHOULD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SHOULD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MORALITY->SHOULD"}]->(child);
```