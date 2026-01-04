// Generated from NO-WATER.md
CREATE (t:THOUGHT {
    name: "thought.NO_WATER",
    alias: "Thought: NO WATER",
    parent: "topic.PHILOSOPHY",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NO_WATER",
    en_title: "NO WATER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO_WATER" AND c.name = "content.NO_WATER"
MERGE (t)-[:HAS_CONTENT {name: "edge.NO_WATER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.NO_WATER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PHILOSOPHY->NO_WATER"}]->(child);
