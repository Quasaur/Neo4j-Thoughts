---
name: thought.HOME_SWEET_HOME
alias: "Thought: HOME, SWEET HOME"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- home
- sweet
- safety
- fellowship
- godhead
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HOME_SWEET_HOME",
    alias: "Thought: HOME, SWEET HOME",
    parent: "topic.THE-GOSPEL",
    tags: ["home", "sweet", "safety", "fellowship", "godhead"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HOME_SWEET_HOME",
    en_title: "HOME, SWEET HOME",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HOME_SWEET_HOME" AND c.name = "content.HOME_SWEET_HOME"
MERGE (t)-[:HAS_CONTENT {name: "edge.HOME_SWEET_HOME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.HOME_SWEET_HOME"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->HOME_SWEET_HOME"}]->(child);
```