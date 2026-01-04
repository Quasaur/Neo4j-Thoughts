// Generated from SECRETS.md
CREATE (t:THOUGHT {
    name: "thought.SECRETS",
    alias: "Thought: SECRETS",
    parent: "topic.PSYCHOLOGY",
    tags: ["secrets", "distractions", "eternity", "immortality", "transcendence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SECRETS",
    en_title: "SECRETS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SECRETS" AND c.name = "content.SECRETS"
MERGE (t)-[:HAS_CONTENT {name: "edge.SECRETS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.SECRETS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->SECRETS"}]->(child);
