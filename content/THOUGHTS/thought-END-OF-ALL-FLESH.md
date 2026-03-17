---
type: THOUGHT
name: "thought.END OF ALL FLESH"
alias: "Thought: End Of All Flesh"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "","
 es_title: "Fin de toda carne"
 es_content: ""
 fr_title: "Fin de toute chair"
 fr_content: ""
 hi_title: "सभी मांस का अंत"
 hi_content: ""
 zh_title: "suǒ yǒu ròu tǐ de zhōng jié"
 zh_content: ""
tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.END OF ALL FLESH",
    alias: "Thought: End Of All Flesh",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.END",
    ctype: "THOUGHT",
    en_title: "End Of All Flesh",
    en_content: "",
    es_title: "Fin de toda carne",
    es_content: "",
    fr_title: "Fin de toute chair",
    fr_content: "",
    hi_title: "सभी मांस का अंत",
    hi_content: "",
    zh_title: "suǒ yǒu ròu tǐ de zhōng jié",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.END OF ALL FLESH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE SOVEREIGNTY->END OF ALL FLESH"
RETURN t, parent;
```
