---
name: "thought.LIMITS OF FORGIVENESS"
alias: "Thought: Limits Of Forgiveness"
type: THOUGHT
en_content: "The only people God doesn't forgive are those who don't want to be forgiven."
parent: "topic.GRACE"
tags:
- forgiveness
- grace
- repentance
- will
- mercy
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.LIMITS OF FORGIVENESS",
    alias: "Thought: Limits Of Forgiveness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'repentance', 'will', 'mercy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIMITS OF FORGIVENESS",
    en_title: "Limits Of Forgiveness",
    en_content: "The only people God doesn't forgive are those who don't want to be forgiven.",
    es_title: "TITULO",
    es_content: "CONTENIDO",
    fr_title: "TITRE",
    fr_content: "CONTENU",
    hi_title: "SHIRSHAK",
    hi_content: "SAMAGRI",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIMITS OF FORGIVENESS" AND c.name = "content.LIMITS OF FORGIVENESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIMITS OF FORGIVENESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LIMITS OF FORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LIMITS OF FORGIVENESS" }]->(child);
```
