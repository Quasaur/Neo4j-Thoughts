---
type: THOUGHT
name: "thought.WANTING FORGIVENESS ONLY"
alias: "Thought: Wanting Forgiveness Only"
parent: "topic.LOVE"
en_content: "We want to be forgiven, but we don't want to forgive...how disgusting."
tags: ["forgiveness", "hypocrisy", "attitude", "character", "disgusting"]
ptopic: "[[topic-LOVE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.WANTING FORGIVENESS ONLY",
    alias: "Thought: Wanting Forgiveness Only",
    parent: "topic.LOVE",
    tags: ['forgiveness', 'hypocrisy', 'attitude', 'character', 'disgusting'],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WANTING FORGIVENESS ONLY",
    ctype: "THOUGHT",
    en_title: "Wanting Forgiveness Only",
    en_content: "We want to be forgiven, but we don't want to forgive...how disgusting.",
    es_title: "Queriendo Solo el Perdón",
    es_content: "Queremos ser perdonados, pero no queremos perdonar...qué repugnante.",
    fr_title: "Vouloir Seulement le Pardon",
    fr_content: "Nous voulons être pardonnés, mais nous ne voulons pas pardonner...comme c'est dégoûtant.",
    hi_title: "केवल क्षमा चाहना",
    hi_content: "हम क्षमा पाना चाहते हैं, लेकिन हम क्षमा करना नहीं चाहते...कितना घिनौना।",
    zh_title: "Zhi Xiang Yao Kuanshu",
    zh_content: "Women xiang bei kuanshu, dan women bu xiang kuanshu bieren...duo me eling."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.WANTING FORGIVENESS ONLY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.LOVE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.LOVE->WANTING FORGIVENESS ONLY"
RETURN t, parent;
```
