// Generated from LIVING-RELATIONSHIPS.md
CREATE (t:THOUGHT {
    name: "thought.LIVING_RELATIONSHIPS",
    alias: "Thought: LIVING RELATIONSHIP",
    parent: "topic.PSYCHOLOGY",
    tags: ["live", "relationships", "people", "jesuschrist", "god"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LIVING_RELATIONSHIPS",
    en_title: "LIVING RELATIONSHIP",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIVING_RELATIONSHIPS" AND c.name = "content.LIVING_RELATIONSHIPS"
MERGE (t)-[:HAS_CONTENT {name: "edge.LIVING_RELATIONSHIPS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LIVING_RELATIONSHIPS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->LIVING_RELATIONSHIPS"}]->(child);
