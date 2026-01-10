---
name: "thought.GRACE VS SATAN"
alias: "Thought: Grace Vs Satan"
type: THOUGHT
en_content: "Apart from Grace, what difference is there between me and Satan? He's older and smarter...other than that we're both petty little monsters."
parent: "topic.GRACE"
tags:
- grace
- satan
- human_nature
- humility
- comparison
level: 2
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Aug-2011)
CREATE (t:THOUGHT {
    name: "thought.GRACE VS SATAN",
    alias: "Thought: Grace Vs Satan",
    parent: "topic.GRACE",
    tags: ["grace", "satan", "human_nature", "humility", "comparison"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GRACE VS SATAN",
    en_title: "Grace Vs Satan",
    en_content: "Apart from Grace, what difference is there between me and Satan? He's older and smarter...other than that we're both petty little monsters.",
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
WHERE t.name = "thought.GRACE VS SATAN" AND c.name = "content.GRACE VS SATAN"
MERGE (t)-[:HAS_CONTENT {name: "edge.GRACE VS SATAN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.GRACE VS SATAN"
MERGE (parent)-[:HAS_THOUGHT {name: "GRACE >GRACE VS SATAN"}]->(child);
```
