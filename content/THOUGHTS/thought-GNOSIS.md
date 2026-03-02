---
type: THOUGHT
name: "thought.GNOSIS"
alias: "Thought: GNOSIS"
parent: "topic.FAITH"
tags: ["gnosis", "faith", "immortality", "knowledge", "believe"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
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
    ctype: "THOUGHT",
    en_title: "GNOSIS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GNOSIS" AND c.name = "content.GNOSIS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GNOSIS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.GNOSIS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITH->GNOSIS"}]->(child);
```