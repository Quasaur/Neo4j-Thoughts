// Generated from IN-HIM-WE-LIVE.md
CREATE (t:THOUGHT {
    name: "thought.IN_HIM_WE_LIVE",
    alias: "Thought: IN HIM WE LIVE",
    parent: "topic.CREATION",
    tags: ["creation", "divine", "fulness", "indwelling", "holyspirit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.IN_HIM_WE_LIVE",
    en_title: "IN HIM WE LIVE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.IN_HIM_WE_LIVE" AND c.name = "content.IN_HIM_WE_LIVE"
MERGE (t)-[:HAS_CONTENT {name: "edge.IN_HIM_WE_LIVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.IN_HIM_WE_LIVE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->IN_HIM_WE_LIVE"}]->(child);
