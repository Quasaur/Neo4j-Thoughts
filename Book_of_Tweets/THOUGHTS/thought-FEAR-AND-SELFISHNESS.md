---
type: THOUGHT
name: "thought.FEAR AND SELFISHNESS"
alias: "Thought: Fear And Selfishness"
parent: "topic.PSYCHOLOGY"
en_content: "Fear wouldn't be so debilitating if I were not so selfish."
tags: ["fear", "selfishness", "psychology", "emotion", "character"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2011a)
CREATE (t:THOUGHT {    name: "thought.FEAR AND SELFISHNESS",
    alias: "Thought: Fear And Selfishness",
    parent: "topic.PSYCHOLOGY",
    tags: ['fear', 'selfishness', 'psychology', 'emotion', 'character'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.FEAR AND SELFISHNESS",
    ctype: "THOUGHT",
    en_title: "Fear And Selfishness",
    en_content: "Fear wouldn't be so debilitating if I were not so selfish.",
    es_title: "Miedo Y Egoísmo",
    es_content: "El miedo no sería tan debilitante si yo no fuera tan egoísta.",
    fr_title: "Peur Et Égoïsme",
    fr_content: "La peur ne serait pas si débilitante si je n'étais pas si égoïste.",
    hi_title: "भय और स्वार्थ",
    hi_content: "यदि मैं इतना स्वार्थी न होता तो भय इतना दुर्बल करने वाला न होता।",
    zh_title: "Kǒngju Hé Zìsī",
    zh_content: "Rúguǒ wǒ bù shì zhème zìsī de huà, kǒngju jiù bù huì rúcǐ lìng rén shuāiruò le."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FEAR AND SELFISHNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->FEAR AND SELFISHNESS"
RETURN t, parent;
```
