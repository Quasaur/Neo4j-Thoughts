// Generated from MYSTERY.md
CREATE (t:THOUGHT {
    name: "thought.MYSTERY",
    alias: "Thought: MYSTERY",
    parent: "topic.PSYCHOLOGY",
    tags: ["wife", "mystery", "understanding", "life", "gift"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MYSTERY",
    en_title: "MYSTERY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MYSTERY" AND c.name = "content.MYSTERY"
MERGE (t)-[:HAS_CONTENT {name: "edge.MYSTERY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.MYSTERY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->MYSTERY"}]->(child);
