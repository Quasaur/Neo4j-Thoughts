// Generated from EVERYTHING.md
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING",
    alias: "Thought: EVERYTHING",
    parent: "topic.CREATION",
    tags: ["god", "creator", "all", "kingdom", "cosmos"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING",
    en_title: "EVERYTHING",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVERYTHING" AND c.name = "content.EVERYTHING"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVERYTHING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.EVERYTHING"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->EVERYTHING"}]->(child);
