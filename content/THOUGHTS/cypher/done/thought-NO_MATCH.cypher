// Generated from NO-MATCH.md
CREATE (t:THOUGHT {
    name: "thought.NO_MATCH",
    alias: "Thought: NO MATCH",
    parent: "topic.BEAUTY",
    tags: ["evolution", "science", "religion", "evidence", "faith"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.NO_MATCH",
    en_title: "NO MATCH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO_MATCH" AND c.name = "content.NO_MATCH"
MERGE (t)-[:HAS_CONTENT {name: "edge.NO_MATCH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.NO_MATCH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.BEAUTY->NO_MATCH"}]->(child);
