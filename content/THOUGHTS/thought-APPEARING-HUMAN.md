---
type: THOUGHT
name: "thought.APPEARING HUMAN"
alias: "Thought: Appearing Human"
parent: "topic.EVIL"
en_content: "Beware of those who appear human, but ain't!"
tags: ["deception", "evil", "appearance", "caution", "humanity"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.APPEARING HUMAN",
    alias: "Thought: Appearing Human",
    parent: "topic.EVIL",
    tags: ['deception', 'evil', 'appearance', 'caution', 'humanity'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.APPEARING HUMAN",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.APPEARING HUMAN"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->APPEARING HUMAN"
RETURN t, parent;
```
