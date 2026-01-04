// Generated from QUIET-THE-FLESH.md
CREATE (t:THOUGHT {
    name: "thought.QUIET_THE_FLESH",
    alias: "Thought: QUIET THE FLESH",
    parent: "topic.GRACE",
    tags: ["flesh", "mortify", "crucify", "spirit", "holy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.QUIET_THE_FLESH",
    en_title: "QUIET THE FLESH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.QUIET_THE_FLESH" AND c.name = "content.QUIET_THE_FLESH"
MERGE (t)-[:HAS_CONTENT {name: "edge.QUIET_THE_FLESH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.QUIET_THE_FLESH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->QUIET_THE_FLESH"}]->(child);
