// Generated from SELF-DENIAL.md
CREATE (t:THOUGHT {
    name: "thought.SELF_DENIAL",
    alias: "Thought: SELF-DENIAL",
    parent: "topic.ATTITUDE",
    tags: ["self", "denial", "humility", "deprecation", "worship"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF_DENIAL",
    en_title: "SELF-DENIAL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF_DENIAL" AND c.name = "content.SELF_DENIAL"
MERGE (t)-[:HAS_CONTENT {name: "edge.SELF_DENIAL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.SELF_DENIAL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->SELF_DENIAL"}]->(child);
