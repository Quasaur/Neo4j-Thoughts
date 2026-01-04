// Generated from FORGIVENESS.md
CREATE (t:THOUGHT {
    name: "thought.FORGIVENESS",
    alias: "Thought: FORGIVENESS",
    parent: "topic.MERCY",
    tags: ["forgiveness", "atonement", "propitiation", "thecross", "jesuschrist"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FORGIVENESS",
    en_title: "FORGIVENESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORGIVENESS" AND c.name = "content.FORGIVENESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FORGIVENESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.FORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MERCY->FORGIVENESS"}]->(child);
