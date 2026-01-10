---
name: thought.DESPISING_THE_CROSS
alias: "Thought: DESPISING THE CROSS"
type: THOUGHT
parent: topic.EVIL
tags:
- cross
- salvation
- gospel
- lakeoffire
- jesuschrist
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DESPISING_THE_CROSS",
    alias: "Thought: DESPISING THE CROSS",
    parent: "topic.EVIL",
    tags: ["cross", "salvation", "gospel", "lakeoffire", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DESPISING_THE_CROSS",
    en_title: "DESPISING THE CROSS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DESPISING_THE_CROSS" AND c.name = "content.DESPISING_THE_CROSS"
MERGE (t)-[:HAS_CONTENT {name: "edge.DESPISING_THE_CROSS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DESPISING_THE_CROSS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->DESPISING_THE_CROSS"}]->(child);
```