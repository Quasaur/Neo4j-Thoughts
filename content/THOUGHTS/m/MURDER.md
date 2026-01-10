---
name: thought.MURDER
alias: "Thought: MURDER"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- crime
- punishment
- intent
- kill
- judgment
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MURDER",
    alias: "Thought: MURDER",
    parent: "topic.PSYCHOLOGY",
    tags: ["crime", "punishment", "intent", "kill", "judgment"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MURDER",
    en_title: "MURDER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MURDER" AND c.name = "content.MURDER"
MERGE (t)-[:HAS_CONTENT {name: "edge.MURDER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.MURDER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->MURDER"}]->(child);
```