---
name: thought.INVITE_OR_COMMAND?
alias: "Thought: INVITE OR COMMAND"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- repent
- invite
- command
- gospel
- judgment
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INVITE_OR_COMMAND?",
    alias: "Thought: INVITE OR COMMAND",
    parent: "topic.THE-GOSPEL",
    tags: ["repent", "invite", "command", "gospel", "judgment"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INVITE_OR_COMMAND?",
    en_title: "INVITE OR COMMAND",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INVITE_OR_COMMAND?" AND c.name = "content.INVITE_OR_COMMAND?"
MERGE (t)-[:HAS_CONTENT {name: "edge.INVITE_OR_COMMAND?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.INVITE_OR_COMMAND?"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->INVITE_OR_COMMAND?"}]->(child);
```