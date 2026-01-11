---
name: "thought.ACCOUNTABILITY"
alias: "Thought: Accountability"
type: THOUGHT
en_content: "God doesn't spare you the consequences of my actions."
parent: "topic.MORALITY"
tags:
- accountability
- consequences
- morality
- responsibility
- justice
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Jul-2011c)
CREATE (t:THOUGHT {
    name: "thought.ACCOUNTABILITY",
    alias: "Thought: Accountability",
    parent: "topic.MORALITY",
    tags: ['accountability', 'consequences', 'morality', 'responsibility', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ACCOUNTABILITY",
    en_title: "Accountability",
    en_content: "God doesn't spare you the consequences of my actions.",
    es_title: "Responsabilidad",
    es_content: "Dios no te libra de las consecuencias de mis acciones.",
    fr_title: "Responsabilité",
    fr_content: "Dieu ne t'épargne pas les conséquences de mes actions.",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "भगवान आपको मेरे कार्यों के परिणामों से नहीं बचाते।",
    zh_title: "问责制",
    zh_content: "上帝不会让你免受我行为的后果。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACCOUNTABILITY" AND c.name = "content.ACCOUNTABILITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ACCOUNTABILITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.ACCOUNTABILITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ACCOUNTABILITY" }]->(child);
```
