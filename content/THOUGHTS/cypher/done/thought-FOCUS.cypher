// Generated from FOCUS.md
CREATE (t:THOUGHT {
    name: "thought.FOCUS",
    alias: "Thought: FOCUS",
    parent: "topic.PSYCHOLOGY",
    tags: ["focus", "crisis", "forward", "criticalthinking", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOCUS",
    en_title: "FOCUS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FOCUS" AND c.name = "content.FOCUS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FOCUS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.FOCUS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->FOCUS"}]->(child);
