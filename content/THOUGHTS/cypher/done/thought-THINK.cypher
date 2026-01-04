// Generated from THINK.md
CREATE (t:THOUGHT {
    name: "thought.THINK",
    alias: "Thought: THINK",
    parent: "topic.PSYCHOLOGY",
    tags: ["think", "howto", "cognition", "critical", "logic"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THINK",
    en_title: "THINK",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THINK" AND c.name = "content.THINK"
MERGE (t)-[:HAS_CONTENT {name: "edge.THINK"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.THINK"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->THINK"}]->(child);
