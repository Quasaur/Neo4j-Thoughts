---
type: THOUGHT
name: "thought.DEBT"
alias: "Thought: DEBT"
parent: "topic.ENTITLEMENT"
tags: ["debt", "entitlement", "apocalypse", "worship", "grace"]
ptopic: "[[topic-ENTITLEMENT]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEBT",
    alias: "Thought: DEBT",
    parent: "topic.ENTITLEMENT",
    tags: ["debt", "entitlement", "apocalypse", "worship", "grace"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEBT",
    ctype: "THOUGHT",
    en_title: "DEBT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEBT" AND c.name = "content.DEBT"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEBT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ENTITLEMENT" AND child.name = "thought.DEBT"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ENTITLEMENT->DEBT"}]->(child);
```