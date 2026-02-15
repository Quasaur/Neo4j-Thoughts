---
name: "thought.SELF_DENIAL"
alias: "Thought: SELF-DENIAL"
type: THOUGHT
parent: "topic.ATTITUDE"

tags:
- self
- denial
- humility
- deprecation
- worship
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SELF_DENIAL",
    alias: "Thought: SELF-DENIAL",
    parent: "topic.ATTITUDE",
    tags: ["self", "denial", "humility", "deprecation", "worship"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF_DENIAL",
    en_title: "SELF-DENIAL",
    en_content: "If you can't say \"No\" to Self, you can't say \"Yes\" to God.",
	es_title: "ABNEGACIÓN",
    es_content: "Si no puedes decir \"No\" a ti mismo, no puedes decir \"Sí\" a Dios.",
	fr_title: "ABNÉGATION",
    fr_content: "Si vous ne pouvez pas dire « Non » à vous-même, vous ne pouvez pas dire « Oui » à Dieu.",
	hi_title: "आत्मोत्सर्ग",
    hi_content: "यदि आप स्वयं को \"नहीं\" नहीं कह सकते, तो आप भगवान को \"हाँ\" नहीं कह सकते।",
	zh_title: "zì wǒ fǒu dìng",
    zh_content: "Rúguǒ nǐ bùnéng duì zìjǐ shuō “bù”, nǐ jiù wúfǎ duì shàngdì shuō “shì”."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF_DENIAL" AND c.name = "content.SELF_DENIAL"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SELF_DENIAL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.SELF_DENIAL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->SELF_DENIAL"}]->(child);
```
