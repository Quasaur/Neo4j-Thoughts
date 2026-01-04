// Generated from PAINFUL-TRUTH.md
CREATE (t:THOUGHT {
    name: "thought.PAINFUL_TRUTH",
    alias: "Thought: PAINFUL TRUTH",
    parent: "topic.PSYCHOLOGY",
    tags: ["tedx", "russellellis", "whitesupremacy", "change", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PAINFUL_TRUTH",
    en_title: "PAINFUL TRUTH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PAINFUL_TRUTH" AND c.name = "content.PAINFUL_TRUTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.PAINFUL_TRUTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.PAINFUL_TRUTH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->PAINFUL_TRUTH"}]->(child);
