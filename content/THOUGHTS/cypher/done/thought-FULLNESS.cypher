// Generated from FULLNESS.md
CREATE (t:THOUGHT {
    name: "thought.FULLNESS",
    alias: "Thought: FULLNESS",
    parent: "topic.GRACE",
    tags: ["spirituality", "fullness", "overflow", "immunity", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FULLNESS",
    en_title: "FULLNESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FULLNESS" AND c.name = "content.FULLNESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FULLNESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FULLNESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->FULLNESS"}]->(child);
