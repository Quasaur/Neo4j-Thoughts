// Generated from FATHER.md
CREATE (t:THOUGHT {
    name: "thought.FATHER",
    alias: "Thought: FATHER",
    parent: "topic.GRACE",
    tags: ["father", "flesh", "spirit", "knowledgeimmortality"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FATHER",
    en_title: "FATHER",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FATHER" AND c.name = "content.FATHER"
MERGE (t)-[:HAS_CONTENT {name: "edge.FATHER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FATHER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->FATHER"}]->(child);
