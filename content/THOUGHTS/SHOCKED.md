---
name: thought.SHOCKED
alias: "Thought: SHOCKED"
type: THOUGHT
parent: topic.EVIL
tags:
- hypocrisy
- shocked
- appalled
- sinner
- sinning
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SHOCKED",
    alias: "Thought: SHOCKED",
    parent: "topic.EVIL",
    tags: ["hypocrisy", "shocked", "appalled", "sinner", "sinning"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SHOCKED",
    en_title: "SHOCKED",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHOCKED" AND c.name = "content.SHOCKED"
MERGE (t)-[:HAS_CONTENT {name: "edge.SHOCKED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.SHOCKED"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->SHOCKED"}]->(child);
```