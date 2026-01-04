// Generated from THE-END-OF-EVIL.md
CREATE (t:THOUGHT {
    name: "thought.THE_END_OF_EVIL",
    alias: "Thought: THE END OF EVIL",
    parent: "topic.EVIL",
    tags: ["day", "evil", "cessation", "hope", "future"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE_END_OF_EVIL",
    en_title: "THE END OF EVIL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_END_OF_EVIL" AND c.name = "content.THE_END_OF_EVIL"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_END_OF_EVIL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.THE_END_OF_EVIL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->THE_END_OF_EVIL"}]->(child);
