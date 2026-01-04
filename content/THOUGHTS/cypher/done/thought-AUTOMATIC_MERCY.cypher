// Generated from AUTOMATIC-MERCY.md
CREATE (t:THOUGHT {
    name: "thought.AUTOMATIC_MERCY",
    alias: "Thought: AUTHOMATIC MERCY",
    parent: "topic.ATTITUDE",
    tags: ["spirituality", "mercy", "hatred", "gospel", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AUTOMATIC_MERCY",
    en_title: "AUTHOMATIC MERCY",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AUTOMATIC_MERCY" AND c.name = "content.AUTOMATIC_MERCY"
MERGE (t)-[:HAS_CONTENT {name: "edge.AUTOMATIC_MERCY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.AUTOMATIC_MERCY"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->AUTOMATIC_MERCY"}]->(child);
