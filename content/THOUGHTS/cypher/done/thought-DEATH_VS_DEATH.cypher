// Generated from DEATH-VS-DEATH.md
CREATE (t:THOUGHT {
    name: "thought.DEATH_VS_DEATH",
    alias: "Thought: DEATH VS DEATH",
    parent: "topic.THE-GOSPEL",
    tags: ["death", "destroy", "idea", "god", "eternallife"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DEATH_VS_DEATH",
    en_title: "DEATH VS DEATH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEATH_VS_DEATH" AND c.name = "content.DEATH_VS_DEATH"
MERGE (t)-[:HAS_CONTENT {name: "edge.DEATH_VS_DEATH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.DEATH_VS_DEATH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->DEATH_VS_DEATH"}]->(child);
