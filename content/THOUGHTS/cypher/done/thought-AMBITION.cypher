// Generated from AMBITION.md
CREATE (t:THOUGHT {
    name: "thought.AMBITION",
    alias: "Thought: AMBITION",
    parent: "topic.THE-GOSPEL",
    tags: ["dailyroutine", "eating", "sleeping", "working", "discipline"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.AMBITION",
    en_title: "AMBITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMBITION" AND c.name = "content.AMBITION"
MERGE (t)-[:HAS_CONTENT {name: "edge.AMBITION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.AMBITION"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->AMBITION"}]->(child);
