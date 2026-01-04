// Generated from HAPPY-SABBATH.md
CREATE (t:THOUGHT {
    name: "thought.HAPPY_SABBATH",
    alias: "Thought: HAPPY SABBATH",
    parent: "topic.CREATION",
    tags: ["happy", "sabbath", "earth", "creation", "rest"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HAPPY_SABBATH",
    en_title: "HAPPY SABBATH",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HAPPY_SABBATH" AND c.name = "content.HAPPY_SABBATH"
MERGE (t)-[:HAS_CONTENT {name: "edge.HAPPY_SABBATH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.HAPPY_SABBATH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.CREATION->HAPPY_SABBATH"}]->(child);
