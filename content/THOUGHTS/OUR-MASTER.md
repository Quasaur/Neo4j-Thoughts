---
name: thought.OUR_MASTER
alias: "Thought: OUR MASTER"
type: THOUGHT
parent: topic.TRUTH
tags:
- truth
- master
- seovereign
- veritas
- ultimate
neo4j: true
ptopic: "[[topic-TRUTH]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.OUR_MASTER",
    alias: "Thought: OUR MASTER",
    parent: "topic.TRUTH",
    tags: ["truth", "master", "seovereign", "veritas", "ultimate"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OUR_MASTER",
    en_title: "OUR MASTER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OUR_MASTER" AND c.name = "content.OUR_MASTER"
MERGE (t)-[:HAS_CONTENT {name: "edge.OUR_MASTER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.OUR_MASTER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.TRUTH->OUR_MASTER"}]->(child);
```