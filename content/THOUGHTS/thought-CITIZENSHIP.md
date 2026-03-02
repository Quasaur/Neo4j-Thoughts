---
type: THOUGHT
name: "thought.CITIZENSHIP"
alias: "Thought: CITIZENSHIP"
parent: "topic.ECONOMICS"
tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"]
ptopic: "[[topic-ECONOMICS]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.CITIZENSHIP",
    alias: "Thought: CITIZENSHIP",
    parent: "topic.ECONOMICS",
    tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CITIZENSHIP",
    ctype: "THOUGHT",
    en_title: "CITIZENSHIP",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CITIZENSHIP" AND c.name = "content.CITIZENSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.CITIZENSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ECONOMICS" AND child.name = "thought.CITIZENSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ECONOMICS->CITIZENSHIP"}]->(child);
```