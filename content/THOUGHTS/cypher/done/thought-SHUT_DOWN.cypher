// Generated from SHUT-DOWN.md
CREATE (t:THOUGHT {
    name: "thought.SHUT_DOWN",
    alias: "Thought: SHUT DOWN",
    parent: "topic.FREEDOM",
    tags: ["free", "expression", "constitutiion", "rights", "tiktok"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.SHUT_DOWN",
    en_title: "SHUT DOWN",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHUT_DOWN" AND c.name = "content.SHUT_DOWN"
MERGE (t)-[:HAS_CONTENT {name: "edge.SHUT_DOWN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FREEDOM" AND child.name = "thought.SHUT_DOWN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FREEDOM->SHUT_DOWN"}]->(child);
