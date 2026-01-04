// Generated from A-GREAT-DAY.md
CREATE (t:THOUGHT {
    name: "thought.A_GREAT_DAY",
    alias: "Thought: A Great Day",
    parent: "topic.HUMOR",
    tags: ["dailyroutine", "eating", "sleeping", "working", "humor"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.A_GREAT_DAY",
    en_title: "A Great Day",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.A_GREAT_DAY" AND c.name = "content.A_GREAT_DAY"
MERGE (t)-[:HAS_CONTENT {name: "edge.A_GREAT_DAY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.A_GREAT_DAY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMOR->A_GREAT_DAY"}]->(child);
