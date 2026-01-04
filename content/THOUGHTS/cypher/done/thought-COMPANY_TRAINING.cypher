// Generated from COMPANY-TRAINING.md
CREATE (t:THOUGHT {
    name: "thought.COMPANY_TRAINING",
    alias: "Thought: COMPANY TRAINING",
    parent: "topic.PSYCHOLOGY",
    tags: ["time", "training", "courses", "company", "mismanagement"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.COMPANY_TRAINING",
    en_title: "COMPANY TRAINING",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.COMPANY_TRAINING" AND c.name = "content.COMPANY_TRAINING"
MERGE (t)-[:HAS_CONTENT {name: "edge.COMPANY_TRAINING"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.COMPANY_TRAINING"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->COMPANY_TRAINING"}]->(child);
