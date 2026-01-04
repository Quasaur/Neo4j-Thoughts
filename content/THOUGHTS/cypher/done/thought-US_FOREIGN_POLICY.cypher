// Generated from US-FOREIGN-POLICY.md
CREATE (t:THOUGHT {
    name: "thought.US_FOREIGN_POLICY",
    alias: "Thought: DARK US FOREIGN POLICY",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["usa", "foreignpolicy", "govoverthrow", "wrathofgod", "threat"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.US_FOREIGN_POLICY",
    en_title: "DARK US FOREIGN POLICY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.US_FOREIGN_POLICY" AND c.name = "content.US_FOREIGN_POLICY"
MERGE (t)-[:HAS_CONTENT {name: "edge.US_FOREIGN_POLICY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.POLITICAL-SCIENCE" AND child.name = "thought.US_FOREIGN_POLICY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.POLITICAL-SCIENCE->US_FOREIGN_POLICY"}]->(child);
