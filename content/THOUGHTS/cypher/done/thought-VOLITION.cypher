// Generated from VOLITION.md
CREATE (t:THOUGHT {
    name: "thought.VOLITION",
    alias: "Thought: VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["paradox", "volition", "freewill", "fullness", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION",
    en_title: "VOLITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION" AND c.name = "content.VOLITION"
MERGE (t)-[:HAS_CONTENT {name: "edge.VOLITION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->VOLITION"}]->(child);
