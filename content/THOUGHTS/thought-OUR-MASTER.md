---
type: THOUGHT
name: "thought.OUR MASTER"
alias: "Thought: Our Master"
parent: "topic.TRUTH"
en_content: "Truth belongs to no one; It is It's own Master...and ours."
tags: ["truth", "master", "seovereign", "veritas", "ultimate"]
ptopic: "[[topic-TRUTH]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.OUR MASTER",
    alias: "Thought: Our Master",
    parent: "topic.TRUTH",
    tags: ["truth", "master", "seovereign", "veritas", "ultimate"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OUR MASTER",
    ctype: "THOUGHT",
    en_title: "Our Master",
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
WHERE t.name = "thought.OUR MASTER" AND c.name = "content.OUR MASTER"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.OUR MASTER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.OUR MASTER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.TRUTH->OUR MASTER"}]->(child);
```
