---
name: "thought.FAITH AND WEALTH"
alias: "Thought: Faith And Wealth"
type: THOUGHT
en_content: "Faith is the closest we can get to free wealth."
parent: "topic.FAITH"
tags:
- faith
- wealth
- spiritual_riches
- provision
- belief
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Aug-2013b)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND WEALTH",
    alias: "Thought: Faith And Wealth",
    parent: "topic.FAITH",
    tags: ["faith", "wealth", "spiritual_riches", "provision", "belief"],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH AND WEALTH",
    en_title: "Faith And Wealth",
    en_content: "Faith is the closest we can get to free wealth.",
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
WHERE t.name = "thought.FAITH AND WEALTH" AND c.name = "content.FAITH AND WEALTH"
MERGE (t)-[:HAS_CONTENT {name: "edge.FAITH AND WEALTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH AND WEALTH"
MERGE (parent)-[:HAS_THOUGHT {name: "FAITH >FAITH AND WEALTH"}]->(child);
```
