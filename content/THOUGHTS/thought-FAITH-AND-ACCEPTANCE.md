---
type: THOUGHT
name: "thought.FAITH AND ACCEPTANCE"
alias: "Thought: Faith And Acceptance"
parent: "topic.FAITH"
en_content: "The concepts of Acceptance and Faith are irrevocably linked."
tags: ["faith", "acceptance", "trust", "truth", "spirituality"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND ACCEPTANCE",
    alias: "Thought: Faith And Acceptance",
    parent: "topic.FAITH",
    tags: ['faith', 'acceptance', 'trust', 'truth', 'spirituality'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH AND ACCEPTANCE",
    ctype: "THOUGHT",
    en_title: "Faith And Acceptance",
    en_content: "The concepts of Acceptance and Faith are irrevocably linked.",
    es_title: "Fe y aceptación",
    es_content: "Los conceptos de aceptación y fe están indisolublemente unidos.",
    fr_title: "Foi et acceptation",
    fr_content: "Les concepts d'acceptation et de foi sont indissociablement liés.",
    hi_title: "आस्था और स्वीकृति",
    hi_content: "स्वीकृति और विश्वास की अवधारणाएँ अटूट रूप से जुड़ी हुई हैं।",
    zh_title: "Xìnyǎng yǔ jiēnà",
    zh_content: "jiēnà hé xìnyǎng zhè liǎng gè gàiniàn mì bùkěfēn."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FAITH AND ACCEPTANCE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->FAITH AND ACCEPTANCE"
RETURN t, parent;
```
