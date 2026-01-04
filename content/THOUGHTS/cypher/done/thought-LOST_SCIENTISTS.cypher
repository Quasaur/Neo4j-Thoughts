// Generated from LOST-SCIENTISTS.md
CREATE (t:THOUGHT {
    name: "thought.LOST_SCIENTISTS",
    alias: "Thought: LOST SCIENTISTS",
    parent: "topic.COSMOLOGY",
    tags: ["science", "bigbang", "lost", "creatiion", "origin"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOST_SCIENTISTS",
    en_title: "LOST SCIENTISTS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOST_SCIENTISTS" AND c.name = "content.LOST_SCIENTISTS"
MERGE (t)-[:HAS_CONTENT {name: "edge.LOST_SCIENTISTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.LOST_SCIENTISTS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.COSMOLOGY->LOST_SCIENTISTS"}]->(child);
