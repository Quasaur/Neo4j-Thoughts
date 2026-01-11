---
name: '"thought.ACCURATE THEOLOGY"'
alias: '"Thought: Accurate Theology, Easier Life"'
type: THOUGHT
en_content: '"The more accurate our theology, the easier the Christian life gets."'
parent: topic.TRUTH
tags:
  - theology
  - truth
  - christianity
  - clarity
  - wisdom
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Apr-2012b)
CREATE (t:THOUGHT {
    name: "thought.ACCURATE THEOLOGY",
    alias: "Thought: Accurate Theology,  Easier Life",
    parent: "topic.TRUTH",
    tags: ['theology', 'truth', 'christianity', 'clarity', 'wisdom'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ACCURATE THEOLOGY",
    en_title: "Accurate Theology",
    en_content: "The more accurate our theology, the easier the Christian life gets.",
    es_title: "Teología Precisa",
    es_content: "Cuanto más precisa sea nuestra teología, más fácil se vuelve la vida cristiana.",
    fr_title: "Théologie Précise",
    fr_content: "Plus notre théologie est précise, plus la vie chrétienne devient facile.",
    hi_title: "सटीक धर्मशास्त्र",
    hi_content: "हमारा धर्मशास्त्र जितना सटीक होगा, ईसाई जीवन उतना ही आसान होगा।",
    zh_title: "准确的神学",
    zh_content: "我们的神学越准确，基督徒的生活就越容易。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ACCURATE THEOLOGY" AND c.name = "content.ACCURATE THEOLOGY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ACCURATE THEOLOGY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.ACCURATE THEOLOGY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >ACCURATE THEOLOGY" }]->(child);
```
