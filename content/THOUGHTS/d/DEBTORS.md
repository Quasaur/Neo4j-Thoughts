---
name: thought.DEBTORS
alias: "Thought: DEBTORS"
type: THOUGHT
parent: topic.ECONOMICS
tags:
- economics
- nation
- debtors
- slaves
- liability
neo4j: true
ptopic: "[[topic-ECONOMICS]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEBTORS",
    alias: "Thought: DEBTORS",
    parent: "topic.ECONOMICS",
    tags: ["economics", "nation", "debtors", "slaves", "liability"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DEBTORS",
    en_title: "DEBTORS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEBTORS" AND c.name = "content.DEBTORS"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEBTORS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ECONOMICS" AND child.name = "thought.DEBTORS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ECONOMICS->DEBTORS"}]->(child);
```