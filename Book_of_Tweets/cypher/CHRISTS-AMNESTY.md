---
name: "thought.CHRISTS AMNESTY"
alias: "Thought: Christs Amnesty"
type: THOUGHT
en_content: "Humanity's trial is over, and we have been judged. Execution of sentence is nearer than we realize. Christ is God's Only Amnesty."
parent: "topic.GRACE"
tags:
- amnesty
- christ
- judgment
- grace
- humanity
level: 3
neo4j: true
ptopic: 
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Feb-2012)
CREATE (t:THOUGHT {
    name: "thought.CHRISTS AMNESTY",
    alias: "Thought: Christs Amnesty",
    parent: "topic.GRACE",
    tags: ['amnesty', 'christ', 'judgment', 'grace', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRISTS AMNESTY",
    en_title: "Christs Amnesty",
    en_content: "Humanity's trial is over, and we have been judged. Execution of sentence is nearer than we realize. Christ is God's Only Amnesty.",
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
WHERE t.name = "thought.CHRISTS AMNESTY" AND c.name = "content.CHRISTS AMNESTY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRISTS AMNESTY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.CHRISTS AMNESTY"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >CHRISTS AMNESTY" }]->(child);
```
