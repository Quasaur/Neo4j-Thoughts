// Generated from FOSSILS.md
CREATE (t:THOUGHT {
    name: "thought.FOSSILS",
    alias: "Thought: FOSSILS",
    parent: "topic.GEOLOGY",
    tags: ["geology", "fossils", "creationism", "intelligentdesign", "evidence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FOSSILS",
    en_title: "FOSSILS",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FOSSILS" AND c.name = "content.FOSSILS"
MERGE (t)-[:HAS_CONTENT {name: "edge.FOSSILS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GEOLOGY" AND child.name = "thought.FOSSILS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GEOLOGY->FOSSILS"}]->(child);
