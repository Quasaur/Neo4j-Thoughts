// Generated from VOLITION2.md
CREATE (t:THOUGHT {
    name: "thought.VOLITION2",
    alias: "Thought: SECOND VOLITION",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["freedom", "volition", "freewill", "misused", "abused"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.VOLITION2",
    en_title: "SECOND VOLITION",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.VOLITION2" AND c.name = "content.VOLITION2"
MERGE (t)-[:HAS_CONTENT {name: "edge.VOLITION2"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.VOLITION2"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.DIVINE-SOVEREIGNTY->VOLITION2"}]->(child);
