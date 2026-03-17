---
type: THOUGHT
name: "thought.NEED FOR FAITH"
alias: "Thought: Need For Faith"
parent: "topic.FAITH"
en_content: "As long as there is ignorance, there will be a need for faith."
tags: ["faith", "ignorance", "knowledge", "dependence", "philosophy"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.NEED FOR FAITH",
    alias: "Thought: Need For Faith",
    parent: "topic.FAITH",
    tags: ['faith', 'ignorance', 'knowledge', 'dependence', 'philosophy'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.NEED FOR FAITH",
    ctype: "THOUGHT",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NEED FOR FAITH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->NEED FOR FAITH"
RETURN t, parent;
```
