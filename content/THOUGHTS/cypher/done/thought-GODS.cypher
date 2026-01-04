// Generated from GODS.md
CREATE (t:THOUGHT {
    name: "thought.GODS",
    alias: "Thought: GODS",
    parent: "topic.PSYCHOLOGY",
    tags: ["behavior", "intelligence", "power", "mercy", "compassion"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GODS",
    en_title: "GODS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GODS" AND c.name = "content.GODS"
MERGE (t)-[:HAS_CONTENT {name: "edge.GODS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.GODS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->GODS"}]->(child);
