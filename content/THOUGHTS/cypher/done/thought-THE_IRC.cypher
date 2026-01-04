// Generated from THE-IRC.md
CREATE (t:THOUGHT {
    name: "thought.THE_IRC",
    alias: "Thought: THE IRC",
    parent: "topic.FIN-GOV",
    tags: ["government", "finance", "code", "usa", "tax"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE_IRC",
    en_title: "THE IRC",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_IRC" AND c.name = "content.THE_IRC"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_IRC"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FIN-GOV" AND child.name = "thought.THE_IRC"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FIN-GOV->THE_IRC"}]->(child);
