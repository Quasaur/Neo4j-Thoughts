---
name: thought.EVIL_WAS_NECESSARY
alias: "Thought: EVIL WAS NECESSARY"
type: THOUGHT
parent: topic.EVIL
tags:
- lambofgod
- evil
- salvation
- forgiveness
- jesuschrist
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EVIL_WAS_NECESSARY",
    alias: "Thought: EVIL WAS NECESSARY",
    parent: "topic.EVIL",
    tags: ["lambofgod", "evil", "salvation", "forgiveness", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVIL_WAS_NECESSARY",
    en_title: "EVIL WAS NECESSARY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVIL_WAS_NECESSARY" AND c.name = "content.EVIL_WAS_NECESSARY"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVIL_WAS_NECESSARY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.EVIL_WAS_NECESSARY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->EVIL_WAS_NECESSARY"}]->(child);
```