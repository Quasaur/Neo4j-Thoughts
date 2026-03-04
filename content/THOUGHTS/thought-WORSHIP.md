---
type: THOUGHT
name: "thought.WORSHIP"
alias: "Thought: Worship"
parent: "topic.SPIRITUALITY"
tags: ["worship", "praise", "prayer", "fellowship", "eternalfather"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.WORSHIP",
    alias: "Thought: Worship",
    parent: "topic.SPIRITUALITY",
    tags: ["worship", "praise", "prayer", "fellowship", "eternalfather"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.WORSHIP",
    ctype: "THOUGHT",
    en_title: "Worship",
 es_title: "CULTO",
 fr_title: "CULTE",
 hi_title: "पूजा",
 zh_title: "chóng bài",
    en_content: "",
 es_content: "Una vida de oración sin adoración siempre será incompleta; un niño nacido muerto.",
 fr_content: "Une vie de prière sans culte sera toujours incomplète ; un enfant mort-né.",
 hi_content: "आराधना के बिना प्रार्थना जीवन सदैव अधूरा रहेगा; एक मृत बच्चा.",
 zh_content: "méi yǒu jìng bài de dǎo gào shēng huó yǒng yuǎn shì bù wán zhěng de ； méi yǒu jìng bài de dǎo gào shēng huó yǒng yuǎn shì bù wán zhěng de 。 yí gè sǐ chǎn de hái zi"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WORSHIP" AND c.name = "content.WORSHIP"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.WORSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.WORSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITUALITY->WORSHIP"}]->(child);
```