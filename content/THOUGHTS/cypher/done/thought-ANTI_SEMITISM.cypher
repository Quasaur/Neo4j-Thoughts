// Generated from ANTI-SEMITISM.md
CREATE (t:THOUGHT {
    name: "thought.ANTI_SEMITISM",
    alias: "Thought: ANTI-SEMITISM",
    parent: "topic.PSYCHOLOGY",
    tags: ["antisemitism", "antinegro", "antijew", "antiblack", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANTI_SEMITISM",
    en_title: "ANTI-SEMITISM",
    en_content: "# Thought: ANTI-SEMITISM
It is IMPOSSIBLE to truly love The Lord Jesus Christ and simultaneously hate the Jew. GOD NEVER told any Christian to persecute or punish the Jew; nor would GOD condone any white Christian oppressing, marginalizing or murdering the black man."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANTI_SEMITISM" AND c.name = "content.ANTI_SEMITISM"
MERGE (t)-[:HAS_CONTENT {name: "edge.ANTI_SEMITISM"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.ANTI_SEMITISM"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.PSYCHOLOGY->ANTI_SEMITISM"}]->(child);
