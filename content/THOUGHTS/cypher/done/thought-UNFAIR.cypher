// Generated from UNFAIR.md
CREATE (t:THOUGHT {
    name: "thought.UNFAIR",
    alias: "Thought: UNFAIRT",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["god", "unfair", "wise", "bow", "submit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNFAIR",
    en_title: "UNFAIRT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNFAIR" AND c.name = "content.UNFAIR"
MERGE (t)-[:HAS_CONTENT {name: "edge.UNFAIR"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.UNFAIR"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->UNFAIR"}]->(child);
