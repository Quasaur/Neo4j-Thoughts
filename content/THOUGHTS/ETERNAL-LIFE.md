---
name: thought.ETERNAL_LIFE
alias: "Thought: ETERNAL LIFE"
type: THOUGHT
parent: topic.FAITHFULNESS
tags:
- immortality
- eternallife
- promise
- covenant
- god
neo4j: true
ptopic: "[[topic-FAITHFULNESS]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ETERNAL_LIFE",
    alias: "Thought: ETERNAL LIFE",
    parent: "topic.FAITHFULNESS",
    tags: ["immortality", "eternallife", "promise", "covenant", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ETERNAL_LIFE",
    en_title: "ETERNAL LIFE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ETERNAL_LIFE" AND c.name = "content.ETERNAL_LIFE"
MERGE (t)-[:HAS_CONTENT {name: "edge.ETERNAL_LIFE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITHFULNESS" AND child.name = "thought.ETERNAL_LIFE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITHFULNESS->ETERNAL_LIFE"}]->(child);
```