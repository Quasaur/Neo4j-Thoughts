// Generated from GLORY-TO-GOD.md
CREATE (t:THOUGHT {
    name: "thought.GLORY_TO_GOD",
    alias: "Thought: GLORY TO GOD",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["thegloryofgod", "splendor", "purpose", "existence", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLORY_TO_GOD",
    en_title: "GLORY TO GOD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLORY_TO_GOD" AND c.name = "content.GLORY_TO_GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.GLORY_TO_GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.GLORY_TO_GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->GLORY_TO_GOD"}]->(child);
