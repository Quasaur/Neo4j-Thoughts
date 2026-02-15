---
name: "thought.APPEARING HUMAN"
alias: "Thought: Appearing Human"
type: THOUGHT
en_content: "Beware of those who appear human, but ain't!"
parent: "topic.EVIL"
tags:
- deception
- evil
- appearance
- caution
- humanity
level: 4
neo4j: true
ptopic: "[[topic-EVIL]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Dec-2012)
CREATE (t:THOUGHT {
    name: "thought.APPEARING HUMAN",
    alias: "Thought: Appearing Human",
    parent: "topic.EVIL",
    tags: ['deception', 'evil', 'appearance', 'caution', 'humanity'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.APPEARING HUMAN",
    en_title: "Appearing Human",
    en_content: "Beware of those who appear human, but ain't!",
    es_title: "Apariencia Humana",
    es_content: "¡Cuidado con aquellos que parecen humanos, pero no lo son!",
    fr_title: "Apparence Humaine",
    fr_content: "Méfiez-vous de ceux qui paraissent humains, mais ne le sont pas !",
    hi_title: "मानवीय दिखावा",
    hi_content: "उन लोगों से सावधान रहें जो मानव दिखते हैं, लेकिन हैं नहीं!",
    zh_title: "Kànsì rénlèi",
    zh_content: "Xiǎoxīn nàxiē kàn qǐlái xiàng rénlèi, dàn shíjì shang bùshì de!"
});

MATCH (t:THOUGHT {name: "thought.APPEARING HUMAN"})
MATCH (c:CONTENT {name: "content.APPEARING HUMAN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.APPEARING HUMAN" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.APPEARING HUMAN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.EVIL->APPEARING HUMAN" }]->(child);
```
