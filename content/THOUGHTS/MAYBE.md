---
name: thought.MAYBE
alias: "Thought: MAYBE"
type: THOUGHT
parent: topic.MERCY
tags:
- compassion
- pity
- leniency
- kindness
- love
neo4j: true
ptopic: "[[topic-MERCY]]"
level: 5
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MAYBE",
    alias: "Thought: MAYBE",
    parent: "topic.MERCY",
    tags: ["compassion", "pity", "leniency", "kindness", "love"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.MAYBE",
    en_title: "MAYBE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MAYBE" AND c.name = "content.MAYBE"
MERGE (t)-[:HAS_CONTENT {name: "edge.MAYBE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.MAYBE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->MAYBE"}]->(child);
```