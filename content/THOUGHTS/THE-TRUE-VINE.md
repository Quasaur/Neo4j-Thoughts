---
name: "thought.THE_TRUE_VINE"
alias: "Thought: THE TRUE VINE"
type: THOUGHT
parent: topic.SPIRITUALITY
tags:
- spirituality
- bible
- jesuschrist
- nexus
- truevine
neo4j: true
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_TRUE_VINE",
    alias: "Thought: THE TRUE VINE",
    parent: "topic.SPIRITUALITY",
    tags: ["spirituality", "bible", "jesuschrist", "nexus", "truevine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE_TRUE_VINE",
    en_title: "THE TRUE VINE",
    en_content: "In the annals of spirituality EVERYTHING points to Jesus Christ.",
    es_title: "LA VERDADERA VID",
    es_content: "En los anales de la espiritualidad TODO apunta a Jesucristo.",
    fr_title: "LA VRAIE VIGNE",
    fr_content: "Dans les annales de la spiritualité, TOUT pointe vers Jésus-Christ.",
    hi_title: "सच्ची बेल",
    hi_content: "आध्यात्मिकता के इतिहास में हर चीज़ यीशु मसीह की ओर इशारा करती है।",
    zh_title: "zhēn pú táo shù",
    zh_content: "zài líng xìng shǐ cè zhōng ， yī qiè dōu zhǐ xiàng yē sū jī dū 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_TRUE_VINE" AND c.name = "content.THE_TRUE_VINE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_TRUE_VINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE_TRUE_VINE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY->THE_TRUE_VINE"}]->(child);
```
