---
name: "thought.FORGIVING OTHERS PROBLEM"
alias: "Thought: Forgiving Others Problem"
type: THOUGHT
en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?"
parent: "topic.GRACE"
tags:
- forgiveness
- grace
- character
- love
- peace
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING OTHERS PROBLEM",
    alias: "Thought: Forgiving Others Problem",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'character', 'love', 'peace'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING OTHERS PROBLEM",
    en_title: "Forgiving Others Problem",
    en_content: "If a person has received forgiveness from God for EVERY sin, why would they have a problem forgiving anyone else?",
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
WHERE t.name = "thought.FORGIVING OTHERS PROBLEM" AND c.name = "content.FORGIVING OTHERS PROBLEM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FORGIVING OTHERS PROBLEM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FORGIVING OTHERS PROBLEM"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >FORGIVING OTHERS PROBLEM" }]->(child);
```
