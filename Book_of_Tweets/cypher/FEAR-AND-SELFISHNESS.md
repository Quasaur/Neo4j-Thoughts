---
name: "thought.FEAR AND SELFISHNESS"
alias: "Thought: Fear And Selfishness"
type: THOUGHT
en_content: "Fear wouldn't be so debilitating if I were not so selfish."
parent: "topic.PSYCHOLOGY"
tags:
- fear
- selfishness
- psychology
- emotion
- character
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.FEAR AND SELFISHNESS",
    alias: "Thought: Fear And Selfishness",
    parent: "topic.PSYCHOLOGY",
    tags: ['fear', 'selfishness', 'psychology', 'emotion', 'character'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FEAR AND SELFISHNESS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FEAR AND SELFISHNESS" AND c.name = "content.FEAR AND SELFISHNESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FEAR AND SELFISHNESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.FEAR AND SELFISHNESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PSYCHOLOGY >FEAR AND SELFISHNESS" }]->(child);
```
