// Generated from AMERICAN.md
CREATE (t:THOUGHT {
    name: "thought.AMERICAN",
    alias: "Thought: AMERICAN",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["nationalism", "american", "addiction", "dependency", "codependency"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.AMERICAN",
    en_title: "AMERICAN",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMERICAN" AND c.name = "content.AMERICAN"
MERGE (t)-[:HAS_CONTENT {name: "edge.AMERICAN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.POLITICAL-SCIENCE" AND child.name = "thought.AMERICAN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.POLITICAL-SCIENCE->AMERICAN"}]->(child);
