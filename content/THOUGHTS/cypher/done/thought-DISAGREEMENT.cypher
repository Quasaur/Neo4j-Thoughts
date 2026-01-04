// Generated from DISAGREEMENT.md
CREATE (t:THOUGHT {
    name: "thought.DISAGREEMENT",
    alias: "Thought: DISAGREEMENT",
    parent: "topic.FAITH",
    tags: ["faith", "doctrine", "apostasy", "heresy", "conflict"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DISAGREEMENT",
    en_title: "DISAGREEMENT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DISAGREEMENT" AND c.name = "content.DISAGREEMENT"
MERGE (t)-[:HAS_CONTENT {name: "edge.DISAGREEMENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.DISAGREEMENT"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITH->DISAGREEMENT"}]->(child);
