// Generated from ACT-OF-GOD.md
CREATE (t:THOUGHT {
    name: "thought.ACT_OF_GOD",
    alias: "Thought: Act of God",
    parent: "topic.PSYCHOLOGY",
    tags: ["person", "people", "wife", "husband", "imageofgod"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ACT_OF_GOD",
    en_title: "Act of God",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACT_OF_GOD" AND c.name = "content.ACT_OF_GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACT_OF_GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ACT_OF_GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->ACT_OF_GOD"}]->(child);
