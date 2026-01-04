// Generated from FORBIDDEN.md
CREATE (t:THOUGHT {
    name: "thought.FORBIDDEN",
    alias: "Thought: FORBIDDEN",
    parent: "topic.EVIL",
    tags: ["prohibited", "restricted", "banned", "outlawed", "taboo"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FORBIDDEN",
    en_title: "FORBIDDEN",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORBIDDEN" AND c.name = "content.FORBIDDEN"
MERGE (t)-[:HAS_CONTENT {name: "edge.FORBIDDEN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.FORBIDDEN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->FORBIDDEN"}]->(child);
