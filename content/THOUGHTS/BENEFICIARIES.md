---
name: thought.BENEFICIARIES
alias: "Thought: BENEFICIARIES"
type: THOUGHT
parent: topic.EVANGELISM
tags:
- interpersonal
- encounter
- daily
- victims
- beneficiaries
neo4j: true
ptopic: "[[topic-EVANGELISM]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BENEFICIARIES",
    alias: "Thought: BENEFICIARIES",
    parent: "topic.EVANGELISM",
    tags: ["interpersonal", "encounter", "daily", "victims", "beneficiaries"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BENEFICIARIES",
    en_title: "BENEFICIARIES",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BENEFICIARIES" AND c.name = "content.BENEFICIARIES"
MERGE (t)-[:HAS_CONTENT {name: "edge.BENEFICIARIES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVANGELISM" AND child.name = "thought.BENEFICIARIES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVANGELISM->BENEFICIARIES"}]->(child);
```