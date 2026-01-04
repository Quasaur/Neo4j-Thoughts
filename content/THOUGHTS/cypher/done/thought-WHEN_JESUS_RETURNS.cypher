// Generated from WHEN-JESUS-RETURNS.md
CREATE (t:THOUGHT {
    name: "thought.WHEN_JESUS_RETURNS",
    alias: "Thought: WHEN JESUS RETURNS",
    parent: "topic.HISTORY",
    tags: ["apocalypse", "demons", "angels", "spirituality", "life"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.WHEN_JESUS_RETURNS",
    en_title: "WHEN JESUS RETURNS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WHEN_JESUS_RETURNS" AND c.name = "content.WHEN_JESUS_RETURNS"
MERGE (t)-[:HAS_CONTENT {name: "edge.WHEN_JESUS_RETURNS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.WHEN_JESUS_RETURNS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HISTORY->WHEN_JESUS_RETURNS"}]->(child);
