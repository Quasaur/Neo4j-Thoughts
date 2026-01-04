// Generated from REALITY.md
CREATE (t:THOUGHT {
    name: "thought.REALITY",
    alias: "Thought: REALITY",
    parent: "topic.TRUTH",
    tags: ["cosmology", "relativity", "geocentricity", "michelson", "intelligentdesign"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REALITY",
    en_title: "REALITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REALITY" AND c.name = "content.REALITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.REALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.REALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.TRUTH->REALITY"}]->(child);
