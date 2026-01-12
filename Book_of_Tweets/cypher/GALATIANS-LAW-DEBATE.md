---
name: "thought.GALATIANS LAW DEBATE"
alias: "Thought: Galatians Law Debate"
type: THOUGHT
en_content: "The debate of Galatians is not over the law, but whether or not keeping the law will save one WHO HAS ALREADY BROKEN IT."
parent: "topic.RELIGION"
tags:
- galatians
- law
- grace
- bible
- debate
level: 4
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Apr-2013)
CREATE (t:THOUGHT {
    name: "thought.GALATIANS LAW DEBATE",
    alias: "Thought: Galatians Law Debate",
    parent: "topic.RELIGION",
    tags: ['galatians', 'law', 'grace', 'bible', 'debate'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GALATIANS LAW DEBATE",
    en_title: "Galatians Law Debate",
    en_content: "The debate of Galatians is not over the law, but whether or not keeping the law will save one WHO HAS ALREADY BROKEN IT.",
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
WHERE t.name = "thought.GALATIANS LAW DEBATE" AND c.name = "content.GALATIANS LAW DEBATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GALATIANS LAW DEBATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.GALATIANS LAW DEBATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >GALATIANS LAW DEBATE" }]->(child);
```
