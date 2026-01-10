---
name: thought.GLOVES
alias: "Thought: GLOVES"
type: THOUGHT
parent: topic.EVANGELISM
tags:
- vessel
- instrument
- gospel
- missionaries
- believers
neo4j: true
ptopic: "[[topic-EVANGELISM]]"
level: 3
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GLOVES",
    alias: "Thought: GLOVES",
    parent: "topic.EVANGELISM",
    tags: ["vessel", "instrument", "gospel", "missionaries", "believers"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLOVES",
    en_title: "GLOVES",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLOVES" AND c.name = "content.GLOVES"
MERGE (t)-[:HAS_CONTENT {name: "edge.GLOVES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVANGELISM" AND child.name = "thought.GLOVES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVANGELISM->GLOVES"}]->(child);
```