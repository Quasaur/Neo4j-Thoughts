// Generated from DUST.md
CREATE (t:THOUGHT {
    name: "thought.DUST",
    alias: "Thought: DUST",
    parent: "topic.ATTITUDE",
    tags: ["dust", "humanity", "humility", "worth", "dirt"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DUST",
    en_title: "DUST",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DUST" AND c.name = "content.DUST"
MERGE (t)-[:HAS_CONTENT {name: "edge.DUST"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.DUST"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->DUST"}]->(child);
