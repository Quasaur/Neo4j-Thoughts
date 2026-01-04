// Generated from INNER-REALITY.md
CREATE (t:THOUGHT {
    name: "thought.INNER_REALITY",
    alias: "Thought: INNER REALITY",
    parent: "topic.ATTITUDE",
    tags: ["heart", "feelings", "perception", "reaction", "reality"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INNER_REALITY",
    en_title: "INNER REALITY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INNER_REALITY" AND c.name = "content.INNER_REALITY"
MERGE (t)-[:HAS_CONTENT {name: "edge.INNER_REALITY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.INNER_REALITY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->INNER_REALITY"}]->(child);
