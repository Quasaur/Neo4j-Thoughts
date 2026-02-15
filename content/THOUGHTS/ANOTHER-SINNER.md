---
name: "thought.ANOTHER_SINNER"
alias: "Thought: Another Sinner"
type: THOUGHT
parent: "topic.EVIL"
en_content: "Satan is just another sinner."
tags:
- satan
- sinner
- inferior
- god
- christ
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANOTHER_SINNER",
    alias: "Thought: ANOTHER SINNER",
    parent: "topic.EVIL",
    tags: ["satan", "sinner", "inferior", "god", "christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANOTHER_SINNER",
    en_title: "Another Sinner",
    en_content: "Satan is just another sinner.",
	es_title: "OTRO PECADOR",
    es_content: "Satanás es simplemente otro pecador.",
	fr_title: "UN AUTRE PÉCHEUR",
    fr_content: "Satan n'est qu'un autre pécheur.",
	hi_title: "एक और पापी",
    hi_content: "शैतान एक और पापी है.",
	zh_title: "lìng yí gè zuì rén",
    zh_content: "sā dàn zhǐ bù guò shì lìng yí gè zuì rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANOTHER_SINNER" AND c.name = "content.ANOTHER_SINNER"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ANOTHER_SINNER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.ANOTHER_SINNER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->ANOTHER_SINNER"}]->(child);
```
