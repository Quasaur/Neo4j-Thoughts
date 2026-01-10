---
name: thought.GNOSIS
alias: "Thought: GNOSIS"
type: THOUGHT
parent: topic.FAITH
tags:
- gnosis
- faith
- immortality
- knowledge
- believe
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GNOSIS",
    alias: "Thought: GNOSIS",
    parent: "topic.FAITH",
    tags: ["gnosis", "faith", "immortality", "knowledge", "believe"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GNOSIS",
    en_title: "GNOSIS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GNOSIS" AND c.name = "content.GNOSIS"
MERGE (t)-[:HAS_CONTENT {name: "edge.GNOSIS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.GNOSIS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITH->GNOSIS"}]->(child);
```