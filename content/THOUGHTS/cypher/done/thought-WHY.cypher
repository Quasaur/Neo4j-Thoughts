// Generated from WHY.md
CREATE (t:THOUGHT {
    name: "thought.WHY",
    alias: "Thought: WHY",
    parent: "topic.PSYCHOLOGY",
    tags: ["children", "adults", "demanded", "cause", "why"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WHY",
    en_title: "WHY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WHY" AND c.name = "content.WHY"
MERGE (t)-[:HAS_CONTENT {name: "edge.WHY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.WHY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->WHY"}]->(child);
