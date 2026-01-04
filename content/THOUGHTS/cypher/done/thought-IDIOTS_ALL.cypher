// Generated from IDIOTS-ALL.md
CREATE (t:THOUGHT {
    name: "thought.IDIOTS_ALL",
    alias: "Thought: IDIOTS ALL",
    parent: "topic.PSYCHOLOGY",
    tags: ["foolish", "stupid", "humanity", "everyone", "intelligence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.IDIOTS_ALL",
    en_title: "IDIOTS ALL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IDIOTS_ALL" AND c.name = "content.IDIOTS_ALL"
MERGE (t)-[:HAS_CONTENT {name: "edge.IDIOTS_ALL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.IDIOTS_ALL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->IDIOTS_ALL"}]->(child);
