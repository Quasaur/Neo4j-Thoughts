// Generated from NOT-LIKE-ME.md
CREATE (t:THOUGHT {
    name: "thought.NOT_LIKE_ME",
    alias: "Thought: NOT-LIKE-ME",
    parent: "topic.MERCY",
    tags: ["idolatry", "divine", "superior", "fruitofthespirit", "grace"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.NOT_LIKE_ME",
    en_title: "NOT-LIKE-ME",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOT_LIKE_ME" AND c.name = "content.NOT_LIKE_ME"
MERGE (t)-[:HAS_CONTENT {name: "edge.NOT_LIKE_ME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.NOT_LIKE_ME"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.MERCY->NOT_LIKE_ME"}]->(child);
