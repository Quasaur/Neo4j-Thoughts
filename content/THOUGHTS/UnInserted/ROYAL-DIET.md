---
name: thought.ROYAL_DIET
alias: "Thought: DIET01"
type: THOUGHT
parent: topic.HEALTH
tags:
- breakfast
- lunch
- dinner
- king
- prince
neo4j: true
ptopic: "[[topic-HEALTH]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ROYAL_DIET",
    alias: "Thought: DIET01",
    parent: "topic.HEALTH",
    tags: ["breakfast", "lunch", "dinner", "king", "prince"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ROYAL_DIET",
    en_title: "DIET01",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ROYAL_DIET" AND c.name = "content.ROYAL_DIET"
MERGE (t)-[:HAS_CONTENT {name: "edge.ROYAL_DIET"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HEALTH" AND child.name = "thought.ROYAL_DIET"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HEALTH->ROYAL_DIET"}]->(child);
```