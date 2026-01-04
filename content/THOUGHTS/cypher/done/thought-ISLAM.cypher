// Generated from ISLAM.md
CREATE (t:THOUGHT {
    name: "thought.ISLAM",
    alias: "Thought: ISLAM",
    parent: "topic.RELIGION",
    tags: ["islam", "religion", "antichrist", "demonic", "deception"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ISLAM",
    en_title: "ISLAM",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ISLAM" AND c.name = "content.ISLAM"
MERGE (t)-[:HAS_CONTENT {name: "edge.ISLAM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.ISLAM"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.RELIGION->ISLAM"}]->(child);
