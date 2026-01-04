// Generated from MARK-OF-THE-BEAST.md
CREATE (t:THOUGHT {
    name: "thought.MARK_OF_THE_BEAST",
    alias: "Thought: MARK OF THE BEAST",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "sunday", "sabbath", "faith", "works"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MARK_OF_THE_BEAST",
    en_title: "MARK OF THE BEAST",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MARK_OF_THE_BEAST" AND c.name = "content.MARK_OF_THE_BEAST"
MERGE (t)-[:HAS_CONTENT {name: "edge.MARK_OF_THE_BEAST"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.MARK_OF_THE_BEAST"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->MARK_OF_THE_BEAST"}]->(child);
