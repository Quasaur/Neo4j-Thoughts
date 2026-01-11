---
name: "thought.TRUE_FAITH"
alias: "Thought: TRUE FAITH"
type: THOUGHT
parent: topic.FAITH
tags:
- faith
- trust
- confidence
- obedience
- submission
neo4j: true
ptopic: "[[topic-FAITH]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TRUE_FAITH",
    alias: "Thought: TRUE FAITH",
    parent: "topic.FAITH",
    tags: ["faith", "trust", "confidence", "obedience", "submission"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRUE_FAITH",
    en_title: "TRUE FAITH",
    en_content: "True Faith is believing in God enough to place His Revealed Will above my own.",
    es_title: "FE VERDADERA",
    es_content: "La verdadera fe es creer en Dios lo suficiente como para poner Su Voluntad Revelada por encima de la mía.",
    fr_title: "VRAIE FOI",
    fr_content: "La vraie foi consiste à croire suffisamment en Dieu pour placer sa volonté révélée au-dessus de la mienne.",
    hi_title: "सत्य विश्वास",
    hi_content: "सच्चा विश्वास ईश्वर में इतना विश्वास करना है कि उसकी प्रकट इच्छा को अपनी इच्छा से ऊपर रख सकूं।",
    zh_title: "zhēn shí de xìn yǎng",
    zh_content: "zhēn zhèng de xìn yǎng shì duì shàng dì de xìn yǎng ， zú yǐ jiāng tā suǒ qǐ shì de yì zhì zhì yú wǒ zì jǐ de yì zhì zhī shàng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUE_FAITH" AND c.name = "content.TRUE_FAITH"
MERGE (t)-[:HAS_CONTENT {name: "edge.TRUE_FAITH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.TRUE_FAITH"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.FAITH->TRUE_FAITH"}]->(child);
```
