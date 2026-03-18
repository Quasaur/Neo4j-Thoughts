---
type: THOUGHT
name: "thought.NOTHING AND EVERYTHING"
alias: "Thought: Nothing And Everything"
parent: "topic.HUMANITY"
en_content: "I am nothing to God...and yet...I am everything to God."
tags: ["humanity", "god", "value", "identity", "paradox"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Oct-2011a)
CREATE (t:THOUGHT {    name: "thought.NOTHING AND EVERYTHING",
    alias: "Thought: Nothing And Everything",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'god', 'value', 'identity', 'paradox'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.NOTHING AND EVERYTHING",
    ctype: "THOUGHT",
    en_title: "Nothing And Everything",
    en_content: "I am nothing to God...and yet...I am everything to God.",
    es_title: "Nada Y Todo",
    es_content: "No soy nada para Dios...y sin embargo...soy todo para Dios.",
    fr_title: "Rien Et Tout",
    fr_content: "Je ne suis rien pour Dieu...et pourtant...je suis tout pour Dieu.",
    hi_title: "कुछ नहीं और सब कुछ",
    hi_content: "मैं परमेश्वर के लिए कुछ नहीं हूँ...और फिर भी...मैं परमेश्वर के लिए सब कुछ हूँ।",
    zh_title: "Wu You He Yi Qie",
    zh_content: "Wo dui Shen lai shuo shi wu you...ran er...wo dui Shen lai shuo shi yi qie."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.NOTHING AND EVERYTHING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->NOTHING AND EVERYTHING"
RETURN t, parent;
```
