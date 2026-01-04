// Generated from YOUR-KINGDOM.md
CREATE (t:THOUGHT {
    name: "thought.YOUR_KINGDOM",
    alias: "Thought: YOUR KINGDOM",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["kingdom", "heaven", "earth", "destruction", "jesuschrist"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.YOUR_KINGDOM",
    en_title: "YOUR KINGDOM",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.YOUR_KINGDOM" AND c.name = "content.YOUR_KINGDOM"
MERGE (t)-[:HAS_CONTENT {name: "edge.YOUR_KINGDOM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.YOUR_KINGDOM"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->YOUR_KINGDOM"}]->(child);
