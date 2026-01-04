// Generated from RESULTS.md
CREATE (t:THOUGHT {
    name: "thought.RESULTS",
    alias: "Thought: RESULTS",
    parent: "topic.PSYCHOLOGY",
    tags: ["gunviolence", "massshootings", "gunlaws", "nra", "uscongress"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.RESULTS",
    en_title: "RESULTS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.RESULTS" AND c.name = "content.RESULTS"
MERGE (t)-[:HAS_CONTENT {name: "edge.RESULTS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.RESULTS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->RESULTS"}]->(child);
