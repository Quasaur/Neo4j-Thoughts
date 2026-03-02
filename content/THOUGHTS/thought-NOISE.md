---
type: THOUGHT
name: "thought.NOISE"
alias: "Thought: NOISE"
parent: "topic.GRACE"
tags: ["heart", "noise", "voice_of_god", "hearing", "holy_spirit"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.NOISE",
    alias: "Thought: NOISE",
    parent: "topic.GRACE",
    tags: ["heart", "noise", "voice_of_god", "hearing", "holy_spirit"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOISE",
    ctype: "THOUGHT",
    en_title: "NOISE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOISE" AND c.name = "content.NOISE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.NOISE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.NOISE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->NOISE"}]->(child);
```