---
name: "thought.OUR_MASTER"
alias: "Thought: OUR MASTER"
type: THOUGHT
parent: topic.TRUTH
tags:
- truth
- master
- seovereign
- veritas
- ultimate
neo4j: true
ptopic: "[[topic-TRUTH]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.OUR_MASTER",
    alias: "Thought: OUR MASTER",
    parent: "topic.TRUTH",
    tags: ["truth", "master", "seovereign", "veritas", "ultimate"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OUR_MASTER",
    en_title: "OUR MASTER",
    en_content: "Truth belongs to no one; It is It's own Master...and ours.",
    es_title: "NUESTRO MAESTRO",
    es_content: "La verdad no pertenece a nadie; Es su propio Maestro... y el nuestro.",
    fr_title: "NOTRE MAÎTRE",
    fr_content: "La vérité n’appartient à personne ; C'est son propre Maître... et le nôtre.",
    hi_title: "हमारे स्वामी",
    hi_content: "सत्य किसी का नहीं होता; यह अपना स्वामी है...और हमारा है।",
    zh_title: "wǒ men de dà shī",
    zh_content: "zhēn lǐ bù shǔ yú rèn hé rén ； tā shì tā zì jǐ de zhǔ rén …… yě shì wǒ men de zhǔ rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OUR_MASTER" AND c.name = "content.OUR_MASTER"
MERGE (t)-[:HAS_CONTENT {name: "edge.OUR_MASTER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.OUR_MASTER"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.TRUTH->OUR_MASTER"}]->(child);
```
