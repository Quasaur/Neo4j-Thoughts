// Generated from CONSEQUENCES.md
CREATE (t:THOUGHT {
    name: "thought.CONSEQUENCES",
    alias: "Thought: CONSEQUENCES",
    parent: "topic.MERCY",
    tags: ["consequences", "mercy", "sovereignty", "sin", "suffering"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CONSEQUENCES",
    en_title: "CONSEQUENCES",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONSEQUENCES" AND c.name = "content.CONSEQUENCES"
MERGE (t)-[:HAS_CONTENT {name: "edge.CONSEQUENCES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.CONSEQUENCES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MERCY->CONSEQUENCES"}]->(child);
