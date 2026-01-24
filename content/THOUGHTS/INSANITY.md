---
name: thought.INSANITY
alias: "Thought: INSANITY"
type: THOUGHT
parent: topic.PSYCHOLOGY
tags:
- insanity
- madness
- delusion
- narcissism
- fooliishness
neo4j: true
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INSANITY",
    alias: "Thought: INSANITY",
    parent: "topic.PSYCHOLOGY",
    tags: ["insanity", "madness", "delusion", "narcissism", "fooliishness"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSANITY",
    en_title: "INSANITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INSANITY" AND c.name = "content.INSANITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.INSANITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.INSANITY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->INSANITY"}]->(child);
```