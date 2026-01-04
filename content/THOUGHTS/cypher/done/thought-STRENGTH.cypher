// Generated from STRENGTH.md
CREATE (t:THOUGHT {
    name: "thought.STRENGTH",
    alias: "Thought: STRENGTH",
    parent: "topic.ATTITUDE",
    tags: ["power", "virtue", "strength", "endurance", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.STRENGTH",
    en_title: "STRENGTH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.STRENGTH" AND c.name = "content.STRENGTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.STRENGTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.STRENGTH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->STRENGTH"}]->(child);
