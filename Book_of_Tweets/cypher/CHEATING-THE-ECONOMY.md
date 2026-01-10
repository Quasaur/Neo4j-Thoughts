---
name: "thought.CHEATING THE ECONOMY"
alias: "Thought: Cheating The Economy"
type: THOUGHT
en_content: "As long as we feel it necessary to cheat, lie and steal to survive, our economy will never truly prosper."
parent: "topic.MORALITY"
tags:
- cheat
- lie
- steal
- economy
- morality
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012g)
CREATE (t:THOUGHT {
    name: "thought.CHEATING THE ECONOMY",
    alias: "Thought: Cheating The Economy",
    parent: "topic.MORALITY",
    tags: ['cheat', 'lie', 'steal', 'economy', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHEATING THE ECONOMY",
    en_title: "Cheating The Economy",
    en_content: "As long as we feel it necessary to cheat, lie and steal to survive, our economy will never truly prosper.",
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
WHERE t.name = "thought.CHEATING THE ECONOMY" AND c.name = "content.CHEATING THE ECONOMY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHEATING THE ECONOMY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.CHEATING THE ECONOMY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CHEATING THE ECONOMY" }]->(child);
```
