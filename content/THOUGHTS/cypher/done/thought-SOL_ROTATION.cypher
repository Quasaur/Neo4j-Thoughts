// Generated from SOL-ROTATION.md
CREATE (t:THOUGHT {
    name: "thought.SOL_ROTATION",
    alias: "Thought: SOL ROTATION",
    parent: "topic.CREATION",
    tags: ["sol", "sun", "star", "rotation", "axis"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SOL_ROTATION",
    en_title: "SOL ROTATION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SOL_ROTATION" AND c.name = "content.SOL_ROTATION"
MERGE (t)-[:HAS_CONTENT {name: "edge.SOL_ROTATION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SOL_ROTATION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->SOL_ROTATION"}]->(child);
