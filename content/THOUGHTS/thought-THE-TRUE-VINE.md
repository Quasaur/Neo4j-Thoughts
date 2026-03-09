---
type: THOUGHT
name: "thought.THE TRUE VINE"
alias: "Thought: The True Vine"
parent: "topic.SPIRITUALITY"
en_content: "In the annals of spirituality EVERYTHING points to Jesus Christ."
tags: ["spirituality", "bible", "jesus_christ", "nexus", "truevine"]
ptopic: "[[topic-SPIRITUALITY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE TRUE VINE",
    alias: "Thought: The True Vine",
    parent: "topic.SPIRITUALITY",
    tags: ["spirituality", "bible", "jesus_christ", "nexus", "truevine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.THE TRUE VINE",
    ctype: "THOUGHT",
    en_title: "The True Vine",
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
WHERE t.name = "thought.THE TRUE VINE" AND c.name = "content.THE TRUE VINE"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.THE TRUE VINE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.THE TRUE VINE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITUALITY->THE TRUE VINE"}]->(child);
```
