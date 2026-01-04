// Generated from FIRST-RULE.md
CREATE (t:THOUGHT {
    name: "thought.FIRST_RULE",
    alias: "Thought: FIRST RULE",
    parent: "topic.HUMOR",
    tags: ["humor", "comedy", "social", "media", "movie"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FIRST_RULE",
    en_title: "FIRST RULE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIRST_RULE" AND c.name = "content.FIRST_RULE"
MERGE (t)-[:HAS_CONTENT {name: "edge.FIRST_RULE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.FIRST_RULE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMOR->FIRST_RULE"}]->(child);
