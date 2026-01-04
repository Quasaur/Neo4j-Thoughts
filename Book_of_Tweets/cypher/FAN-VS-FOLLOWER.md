---
name: "thought.FAN VS FOLLOWER"
alias: "Thought: Fan Vs Follower"
type: THOUGHT
parent: "topic.SPIRITUALITY"
tags:
- follower
- fan
- christ
- spirituality
- commitment
level: 2
neo4j: true
insert: true
---
# Fan Vs Follower

> [!Thought-en]
> You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!

```Cypher
// Generated from Book6E-FINAL.md (ID: 05-May-2012a)
CREATE (t:THOUGHT {
    name: "thought.FAN VS FOLLOWER",
    alias: "Thought: Fan Vs Follower",
    parent: "topic.SPIRITUALITY",
    tags: ['follower', 'fan', 'christ', 'spirituality', 'commitment'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.FAN VS FOLLOWER",
    en_title: "Fan Vs Follower",
    en_content: "You can be a fan of Christ yet not a follower; but you cannot be a follower and not be a fan!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAN VS FOLLOWER" AND c.name = "content.FAN VS FOLLOWER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAN VS FOLLOWER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.FAN VS FOLLOWER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >FAN VS FOLLOWER" }]->(child);
```