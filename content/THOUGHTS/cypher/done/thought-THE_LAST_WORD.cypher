// Generated from THE-LAST-WORD.md
CREATE (t:THOUGHT {
    name: "thought.THE_LAST_WORD",
    alias: "Thought: THE LAST WORD",
    parent: "topic.THE-GOSPEL",
    tags: ["gospel", "jesuschrist", "livingword", "lastword", "wordofgod"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_LAST_WORD",
    en_title: "THE LAST WORD",
    en_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_LAST_WORD" AND c.name = "content.THE_LAST_WORD"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_LAST_WORD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.THE_LAST_WORD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->THE_LAST_WORD"}]->(child);
