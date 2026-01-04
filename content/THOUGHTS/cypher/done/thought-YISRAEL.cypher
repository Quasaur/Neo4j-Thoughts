// Generated from YISRAEL.md
CREATE (t:THOUGHT {
    name: "thought.YISRAEL",
    alias: "Thought: YISRAEL",
    parent: "topic.HISTORY",
    tags: ["israel", "apartheid", "genocide", "palestinians", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.YISRAEL",
    en_title: "YISRAEL",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.YISRAEL" AND c.name = "content.YISRAEL"
MERGE (t)-[:HAS_CONTENT {name: "edge.YISRAEL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.YISRAEL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HISTORY->YISRAEL"}]->(child);
