// Generated from ACTS-OF-THE-APOSTLES.md
CREATE (t:THOUGHT {
    name: "thought.ACTS_OF_THE_APOSTLES",
    alias: "Thought: Acts of the Apostles",
    parent: "topic.THE-BIBLE",
    tags: ["bible", "luke", "chronology", "geography", "accuracy"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.ACTS_OF_THE_APOSTLES",
    en_title: "Acts of the Apostles",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACTS_OF_THE_APOSTLES" AND c.name = "content.ACTS_OF_THE_APOSTLES"
MERGE (t)-[:HAS_CONTENT {name: "edge.ACTS_OF_THE_APOSTLES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-BIBLE" AND child.name = "thought.ACTS_OF_THE_APOSTLES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-BIBLE->ACTS_OF_THE_APOSTLES"}]->(child);
