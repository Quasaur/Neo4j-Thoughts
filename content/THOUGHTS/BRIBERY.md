---
name: thought.BRIBERY
alias: "Thought: Bribery"
type: THOUGHT
parent: topic.EVIL
tags:
- lobbying
- uscongress
- bribery
- justice
- oligarchy
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.BRIBERY",
    alias: "Thought: Bribery",
    parent: "topic.EVIL",
    tags: ["lobbying", "uscongress", "bribery", "justice", "oligarchy"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.BRIBERY",
    en_title: "Bribery",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BRIBERY" AND c.name = "content.BRIBERY"
MERGE (t)-[:HAS_CONTENT {name: "edge.BRIBERY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.BRIBERY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->BRIBERY"}]->(child);
```