---
type: THOUGHT
name: "thought.THE END OF EVIL"
alias: "Thought: The End of Evil"
parent: "topic.EVIL"
en_content: "The Day is coming when evil will no longer exist."
tags: ["day", "evil", "cessation", "hope", "future"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.THE END OF EVIL",
    alias: "Thought: The End of Evil",
    parent: "topic.EVIL",
    tags: ["day", "evil", "cessation", "hope", "future"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE END OF EVIL",
    ctype: "THOUGHT",
    en_title: "The End of Evil",
    en_content: "The Day is coming when evil will no longer exist.",
    es_title: "EL FIN DEL MAL",
    es_content: "Se acerca el día en que el mal ya no existirá.",
    fr_title: "LA FIN DU MAL",
    fr_content: "Le jour vient où le mal n’existera plus.",
    hi_title: "बुराई का अंत",
    hi_content: "वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।",
    zh_title: "xié è de zhōng jié",
    zh_content: "The Day is coming when evil will no longer exist."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.THE END OF EVIL"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->THE END OF EVIL"
RETURN t, parent;
```
