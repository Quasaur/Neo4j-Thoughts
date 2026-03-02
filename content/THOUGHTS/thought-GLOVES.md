---
type: THOUGHT
name: "thought.GLOVES"
alias: "Thought: GLOVES"
parent: "topic.EVANGELISM"
tags: ["vessel", "instrument", "gospel", "missionaries", "believers"]
ptopic: "[[topic-EVANGELISM]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GLOVES",
    alias: "Thought: GLOVES",
    parent: "topic.EVANGELISM",
    tags: ["vessel", "instrument", "gospel", "missionaries", "believers"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GLOVES",
    ctype: "THOUGHT",
    en_title: "GLOVES",
    en_content: "God is not looking for hands...He's looking for gloves!",
 es_title: "GUANTES",
 es_content: "Dios no busca manos... ¡Busca guantes!",
 fr_title: "GANTS",
 fr_content: "Dieu ne cherche pas des mains... Il cherche des gants !",
 hi_title: "दस्ताने",
 hi_content: "भगवान हाथों की तलाश में नहीं है...वह दस्ताने की तलाश में है!",
 zh_title: "shǒu tào",
 zh_content: "shàng dì bú shì zài xún zhǎo shuāng shǒu …… tā shì zài xún zhǎo shǒu tào ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLOVES" AND c.name = "content.GLOVES"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GLOVES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVANGELISM" AND child.name = "thought.GLOVES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVANGELISM->GLOVES"}]->(child);
```