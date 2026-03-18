---
type: THOUGHT
name: "thought.NATURE OF THE GODHEAD"
alias: "Thought: Nature Of The Godhead"
parent: "topic.THE GODHEAD"
en_content: "Anyone who thinks they understand the Nature of the Godhead is a liar."
tags: ["godhead", "mystery", "truth", "knowledge", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Jan-2012)
CREATE (t:THOUGHT {    name: "thought.NATURE OF THE GODHEAD",
    alias: "Thought: Nature Of The Godhead",
    parent: "topic.THE GODHEAD",
    tags: ['godhead', 'mystery', 'truth', 'knowledge', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.NATURE OF THE GODHEAD",
    ctype: "THOUGHT",
    en_title: "Nature Of The Godhead",
    en_content: "Anyone who thinks they understand the Nature of the Godhead is a liar.",
    es_title: "Naturaleza de la Divinidad",
    es_content: "Cualquiera que piense que entiende la Naturaleza de la Divinidad es un mentiroso.",
    fr_title: "Nature de la Divinité",
    fr_content: "Quiconque pense comprendre la Nature de la Divinité est un menteur.",
    hi_title: "ईश्वरत्व की प्रकृति",
    hi_content: "जो कोई भी सोचता है कि वे ईश्वरत्व की प्रकृति को समझते हैं, वह झूठा है।",
    zh_title: "Shén xìng de běn zhì",
    zh_content: "Rèn hé rén rú guǒ rèn wéi tā men lǐ jiě Shén xìng de běn zhì, nà me tā men jiù shì shuō huǎng zhě."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NATURE OF THE GODHEAD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->NATURE OF THE GODHEAD"
RETURN t, parent;
```
