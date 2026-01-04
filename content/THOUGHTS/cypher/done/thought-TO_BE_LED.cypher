// Generated from TO_BE_LED.md
CREATE (t:THOUGHT {
    name: "thought.TO_BE_LED",
    alias: "Thought: TO BE LED",
    parent: "topic.GRACE",
    tags: ["led", "follow", "leadership", "holyspirit", "travel"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TO_BE_LED",
    en_title: "TO BE LED",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TO_BE_LED" AND c.name = "content.TO_BE_LED"
MERGE (t)-[:HAS_CONTENT {name: "edge.TO_BE_LED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TO_BE_LED"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->TO_BE_LED"}]->(child);
