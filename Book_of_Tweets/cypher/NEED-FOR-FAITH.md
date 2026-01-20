---
name: "thought.NEED FOR FAITH"
alias: "Thought: Need For Faith"
type: THOUGHT
en_content: "As long as there is ignorance, there will be a need for faith."
parent: "topic.FAITH"
tags:
- faith
- ignorance
- knowledge
- dependence
- philosophy
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.NEED FOR FAITH",
    alias: "Thought: Need For Faith",
    parent: "topic.FAITH",
    tags: ['faith', 'ignorance', 'knowledge', 'dependence', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NEED FOR FAITH",
    en_title: "Need For Faith",
    en_content: "As long as there is ignorance, there will be a need for faith.",
    es_title: "Necesidad de Fe",
    es_content: "Mientras exista la ignorancia, habrá necesidad de fe.",
    fr_title: "Besoin de Foi",
    fr_content: "Tant qu'il y aura de l'ignorance, il y aura un besoin de foi.",
    hi_title: "विश्वास की आवश्यकता",
    hi_content: "जब तक अज्ञानता है, तब तक विश्वास की आवश्यकता रहेगी।",
    zh_title: "Xìnyǎng de Xūyào",
    zh_content: "Zhǐyào cúnzài wúzhī, jiù xūyào xìnyǎng."
});

MATCH (t:THOUGHT {name: "thought.NEED FOR FAITH"})
MATCH (c:CONTENT {name: "content.NEED FOR FAITH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.NEED FOR FAITH" }]->(c);

MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:THOUGHT {name: "thought.NEED FOR FAITH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >NEED FOR FAITH" }]->(child);
```
