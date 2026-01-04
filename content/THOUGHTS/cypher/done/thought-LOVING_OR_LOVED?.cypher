// Generated from LOVING-OR-LOVED?.md
CREATE (t:THOUGHT {
    name: "thought.LOVING_OR_LOVED?",
    alias: "Thought: LOVING OR LOVED?",
    parent: "topic.PSYCHOLOGY",
    tags: ["loving", "loved", "give", "receive", "preference"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LOVING_OR_LOVED?",
    en_title: "LOVING OR LOVED?",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVING_OR_LOVED?" AND c.name = "content.LOVING_OR_LOVED?"
MERGE (t)-[:HAS_CONTENT {name: "edge.LOVING_OR_LOVED?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.LOVING_OR_LOVED?"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->LOVING_OR_LOVED?"}]->(child);
