// Generated from THE-TRUE-VINE.md
CREATE (t:THOUGHT {
    name: "thought.THE_TRUE_VINE",
    alias: "Thought: THE TRUE VINE",
    parent: "topic.SPIRITUALITY",
    tags: ["spirituality", "bible", "jesuschrist", "nexus", "truevine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_TRUE_VINE",
    en_title: "THE TRUE VINE",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_TRUE_VINE" AND c.name = "content.THE_TRUE_VINE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_TRUE_VINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE_TRUE_VINE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->THE_TRUE_VINE"}]->(child);
