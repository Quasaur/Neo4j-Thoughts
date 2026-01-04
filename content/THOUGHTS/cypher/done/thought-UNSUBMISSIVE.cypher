// Generated from UNSUBMISSIVE.md
CREATE (t:THOUGHT {
    name: "thought.UNSUBMISSIVE",
    alias: "Thought: UNSUBMISSIVE",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["unsubmissive", "rebellious", "pointless", "meaningless", "god"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNSUBMISSIVE",
    en_title: "UNSUBMISSIVE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNSUBMISSIVE" AND c.name = "content.UNSUBMISSIVE"
MERGE (t)-[:HAS_CONTENT {name: "edge.UNSUBMISSIVE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.UNSUBMISSIVE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->UNSUBMISSIVE"}]->(child);
