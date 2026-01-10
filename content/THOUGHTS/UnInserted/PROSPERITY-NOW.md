---
name: thought.PROSPERITY_NOW
alias: "Thought: PROSPERITY NOW"
type: THOUGHT
parent: topic.RELIGION
tags:
- prosperity
- faith
- prayer
- supplication
- sorcery
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PROSPERITY_NOW",
    alias: "Thought: PROSPERITY NOW",
    parent: "topic.RELIGION",
    tags: ["prosperity", "faith", "prayer", "supplication", "sorcery"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PROSPERITY_NOW",
    en_title: "PROSPERITY NOW",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PROSPERITY_NOW" AND c.name = "content.PROSPERITY_NOW"
MERGE (t)-[:HAS_CONTENT {name: "edge.PROSPERITY_NOW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.PROSPERITY_NOW"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.RELIGION->PROSPERITY_NOW"}]->(child);
```