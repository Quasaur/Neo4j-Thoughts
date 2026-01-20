---
name: "thought.NATURE OF THE GODHEAD"
alias: "Thought: Nature Of The Godhead"
type: THOUGHT
en_content: "Anyone who thinks they understand the Nature of the Godhead is a liar."
parent: "topic.THE GODHEAD"
tags:
- godhead
- mystery
- truth
- knowledge
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NATURE OF THE GODHEAD",
    alias: "Thought: Nature Of The Godhead",
    parent: "topic.THE GODHEAD",
    tags: ['godhead', 'mystery', 'truth', 'knowledge', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NATURE OF THE GODHEAD",
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

MATCH (t:THOUGHT {name: "thought.NATURE OF THE GODHEAD"})
MATCH (c:CONTENT {name: "content.NATURE OF THE GODHEAD"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NATURE OF THE GODHEAD" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.NATURE OF THE GODHEAD"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NATURE OF THE GODHEAD" }]->(child);
```
