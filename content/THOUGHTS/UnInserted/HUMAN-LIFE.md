---
name: thought.HUMAN_LIFE
alias: "Thought: HUMAN LIFE"
type: THOUGHT
parent: topic.WORSHIP
tags:
- humanity
- godhead
- intelligent
- life
- purpose
neo4j: true
ptopic: "[[topic-WORSHIP]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN_LIFE",
    alias: "Thought: HUMAN LIFE",
    parent: "topic.WORSHIP",
    tags: ["humanity", "godhead", "intelligent", "life", "purpose"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN_LIFE",
    en_title: "HUMAN LIFE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN_LIFE" AND c.name = "content.HUMAN_LIFE"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN_LIFE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WORSHIP" AND child.name = "thought.HUMAN_LIFE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.WORSHIP->HUMAN_LIFE"}]->(child);
```