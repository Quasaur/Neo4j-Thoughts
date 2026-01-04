// Generated from NOISE.md
CREATE (t:THOUGHT {
    name: "thought.NOISE",
    alias: "Thought: NOISE",
    parent: "topic.GRACE",
    tags: ["heart", "noise", "voiceofgod", "hearing", "holyspirit"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOISE",
    en_title: "NOISE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOISE" AND c.name = "content.NOISE"
MERGE (t)-[:HAS_CONTENT {name: "edge.NOISE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.NOISE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->NOISE"}]->(child);
