// Generated from DIVINE-WORTH.md
CREATE (t:THOUGHT {
    name: "thought.DIVINE_WORTH",
    alias: "Thought: DIVINE WORTH",
    parent: "topic.HOLINESS",
    tags: ["deity", "holy", "worth", "value", "diine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE_WORTH",
    en_title: "DIVINE WORTH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIVINE_WORTH" AND c.name = "content.DIVINE_WORTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE_WORTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HOLINESS" AND child.name = "thought.DIVINE_WORTH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HOLINESS->DIVINE_WORTH"}]->(child);
