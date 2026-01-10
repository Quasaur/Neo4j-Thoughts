---
name: thought.WORSHIP
alias: "Thought: WORSHIP"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- worship
- praise
- prayer
- fellowship
- eternalfather
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WORSHIP",
    alias: "Thought: WORSHIP",
    parent: "topic.SPIRITUALITY",
    tags: ["worship", "praise", "prayer", "fellowship", "eternalfather"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WORSHIP",
    en_title: "WORSHIP",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WORSHIP" AND c.name = "content.WORSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.WORSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.WORSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->WORSHIP"}]->(child);
```