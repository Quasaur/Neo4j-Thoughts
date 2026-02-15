---
name: "thought.FIRST_RULE"
alias: "Thought: FIRST RULE"
type: THOUGHT
parent: "topic.HUMOR"
en_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter)."
tags:
- humor
- comedy
- social
- media
- movie
neo4j: true
ptopic: "[[topic-HUMOR]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FIRST_RULE",
    alias: "Thought: FIRST RULE",
    parent: "topic.HUMOR",
    tags: ["humor", "comedy", "social", "media", "movie"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FIRST_RULE",
    en_title: "FIRST RULE",
    en_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter).",
	es_title: "PRIMERA REGLA",
    es_content: "Primera regla de Twitter: no se habla de Facebook. Morir de risa.",
	fr_title: "PREMIÈRE RÈGLE",
    fr_content: "Première règle de Twitter : on ne parle pas de Facebook. Mourir de rire.",
	hi_title: "पहला नियम",
    hi_content: "First rule of Twitter: you do not talk about FaceBook. (dying of laughter).",
	zh_title: "dì yī tiáo guī zé",
    zh_content: "Twitter  de dì yī tiáo guī zé ： nǐ bù néng tán lùn  Facebook。 xiào sǐ le 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIRST_RULE" AND c.name = "content.FIRST_RULE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FIRST_RULE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.FIRST_RULE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HUMOR->FIRST_RULE"}]->(child);
```
