// Generated from THE-LAKE-OF-FIRE-AND-SULFUR.md
CREATE (t:THOUGHT {
    name: "thought.THE_LAKE_OF_FIRE_AND_SULFUR",
    alias: "Thought: THE LAKE OF FIRE AND SULFUR",
    parent: "topic.JUSTICE",
    tags: ["lakeoffire", "wrathofgod", "hell", "regret", "eternity"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE_LAKE_OF_FIRE_AND_SULFUR",
    en_title: "THE LAKE OF FIRE AND SULFUR",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_LAKE_OF_FIRE_AND_SULFUR" AND c.name = "content.THE_LAKE_OF_FIRE_AND_SULFUR"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_LAKE_OF_FIRE_AND_SULFUR"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.THE_LAKE_OF_FIRE_AND_SULFUR"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.JUSTICE->THE_LAKE_OF_FIRE_AND_SULFUR"}]->(child);
