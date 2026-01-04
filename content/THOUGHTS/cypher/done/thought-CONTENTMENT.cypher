// Generated from CONTENTMENT.md
CREATE (t:THOUGHT {
    name: "thought.CONTENTMENT",
    alias: "Thought: CONTENTMENT",
    parent: "topic.ATTITUDE",
    tags: ["contentment", "acceptance", "carefree", "failure", "faith"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CONTENTMENT",
    en_title: "CONTENTMENT",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONTENTMENT" AND c.name = "content.CONTENTMENT"
MERGE (t)-[:HAS_CONTENT {name: "edge.CONTENTMENT"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.CONTENTMENT"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.ATTITUDE->CONTENTMENT"}]->(child);
