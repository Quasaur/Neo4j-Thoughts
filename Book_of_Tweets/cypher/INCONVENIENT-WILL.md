---
name: "thought.INCONVENIENT WILL"
alias: "Thought: Inconvenient Will"
type: THOUGHT
en_content: "Accomplishing God's Will is rarely convenient."
parent: "topic.SPIRITUALITY"
tags:
- will
- obedience
- spirituality
- sacrifice
- convenience
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.INCONVENIENT WILL",
    alias: "Thought: Inconvenient Will",
    parent: "topic.SPIRITUALITY",
    tags: ['will', 'obedience', 'spirituality', 'sacrifice', 'convenience'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INCONVENIENT WILL",
    en_title: "Inconvenient Will",
    en_content: "Accomplishing God's Will is rarely convenient.",
    es_title: "Voluntad Inconveniente",
    es_content: "Cumplir la Voluntad de Dios rara vez es conveniente.",
    fr_title: "Volonté Incommode",
    fr_content: "Accomplir la Volonté de Dieu est rarement pratique.",
    hi_title: "असुविधाजनक इच्छा",
    hi_content: "परमेश्वर की इच्छा को पूरा करना शायद ही कभी सुविधाजनक होता है।",
    zh_title: "Bù Biàn de Yìzhì",
    zh_content: "Chéngjiù Shàngdì de Yìzhì hěn shǎo shì fāngbiàn de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INCONVENIENT WILL" AND c.name = "content.INCONVENIENT WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCONVENIENT WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.INCONVENIENT WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >INCONVENIENT WILL" }]->(child);
```
