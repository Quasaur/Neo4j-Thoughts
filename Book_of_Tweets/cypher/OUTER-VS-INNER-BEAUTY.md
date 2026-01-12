---
name: "thought.OUTER VS INNER BEAUTY"
alias: "Thought: Outer Vs Inner Beauty"
type: THOUGHT
en_content: "Outer beauty doesn't make up for inner ugly."
parent: "topic.BEAUTY"
tags:
- beauty
- character
- appearance
- aesthetics
- holiness
level: 5
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.OUTER VS INNER BEAUTY",
    alias: "Thought: Outer Vs Inner Beauty",
    parent: "topic.BEAUTY",
    tags: ['beauty', 'character', 'appearance', 'aesthetics', 'holiness'],
    notes: "",
    level: 5
});

CREATE (c:CONTENT {
    name: "content.OUTER VS INNER BEAUTY",
    en_title: "Outer Vs Inner Beauty",
    en_content: "Outer beauty doesn't make up for inner ugly.",
    es_title: "Belleza Exterior Vs Interior",
    es_content: "La belleza exterior no compensa la fealdad interior.",
    fr_title: "Beauté Extérieure Vs Intérieure",
    fr_content: "La beauté extérieure ne compense pas la laideur intérieure.",
    hi_title: "बाहरी बनाम भीतरी सुंदरता",
    hi_content: "बाहरी सुंदरता भीतरी कुरूपता की भरपाई नहीं करती।",
    zh_title: "Wai Zai Mei Yu Nei Zai Mei",
    zh_content: "Wai zai de mei li bu neng mi bu nei zai de chou lou."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OUTER VS INNER BEAUTY" AND c.name = "content.OUTER VS INNER BEAUTY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OUTER VS INNER BEAUTY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.BEAUTY" AND child.name = "thought.OUTER VS INNER BEAUTY"
MERGE (parent)-[:HAS_THOUGHT { "name": "BEAUTY >OUTER VS INNER BEAUTY" }]->(child);
```
