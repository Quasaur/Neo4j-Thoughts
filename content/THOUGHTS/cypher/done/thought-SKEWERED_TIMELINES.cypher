// Generated from SKEWERED-TIMELINES.md
CREATE (t:THOUGHT {
    name: "thought.SKEWERED_TIMELINES",
    alias: "Thought: SKEWERED TIMELINES",
    parent: "topic.HISTORY",
    tags: ["evolution", "pseudoscience", "timelines", "religion", "creation"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SKEWERED_TIMELINES",
    en_title: "SKEWERED TIMELINES",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SKEWERED_TIMELINES" AND c.name = "content.SKEWERED_TIMELINES"
MERGE (t)-[:HAS_CONTENT {name: "edge.SKEWERED_TIMELINES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.SKEWERED_TIMELINES"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HISTORY->SKEWERED_TIMELINES"}]->(child);
