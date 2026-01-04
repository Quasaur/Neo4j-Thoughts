// Generated from EVOLUTION-IS-SCIENCE?.md
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION_IS_SCIENCE?",
    alias: "Thought: EVOLUTION IS SCIENCE?",
    parent: "topic.RELIGION",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION_IS_SCIENCE?",
    en_title: "EVOLUTION IS SCIENCE?",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EVOLUTION_IS_SCIENCE?" AND c.name = "content.EVOLUTION_IS_SCIENCE?"
MERGE (t)-[:HAS_CONTENT {name: "edge.EVOLUTION_IS_SCIENCE?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.EVOLUTION_IS_SCIENCE?"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.RELIGION->EVOLUTION_IS_SCIENCE?"}]->(child);
