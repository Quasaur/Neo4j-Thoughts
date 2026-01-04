// Generated from DEMONS.md
CREATE (t:THOUGHT {
    name: "thought.DEMONS",
    alias: "Thought: DEMONS",
    parent: "topic.SPIRITS",
    tags: ["demons", "hardhearted", "grace", "divine", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEMONS",
    en_title: "DEMONS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEMONS" AND c.name = "content.DEMONS"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEMONS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.DEMONS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITS->DEMONS"}]->(child);
