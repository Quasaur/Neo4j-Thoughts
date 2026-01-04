// Generated from POINTLESS.md
CREATE (t:THOUGHT {
    name: "thought.POINTLESS",
    alias: "Thought: POINTLESS",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["pointless", "purpose", "meaning", "god", "sovereignty"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.POINTLESS",
    en_title: "POINTLESS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.POINTLESS" AND c.name = "content.POINTLESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.POINTLESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.POINTLESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->POINTLESS"}]->(child);
