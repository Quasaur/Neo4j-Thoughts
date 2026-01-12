---
name: "thought.REJOICING IN OTHERS"
alias: "Thought: Rejoicing In Others"
type: THOUGHT
en_content: I rejoice in the achievements God accomplished in you as though He had accomplished them in me.
parent: topic.LOVE
tags:
  - joy
  - character
  - comparison
  - attitude
  - success
level: 3
neo4j: true
ptopic: "[[topic-LOVE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Dec-2011b)
CREATE (t:THOUGHT {
    name: "thought.REJOICING IN OTHERS",
    alias: "Thought: Rejoicing In Others",
    parent: "topic.ATTITUDE",
    tags: ['joy', 'character', 'comparison', 'attitude', 'success'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.REJOICING IN OTHERS",
    en_title: "Rejoicing In Others",
    en_content: "I rejoice in the achievements God accomplished in you as though He had accomplished them in me.",
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
WHERE t.name = "thought.REJOICING IN OTHERS" AND c.name = "content.REJOICING IN OTHERS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJOICING IN OTHERS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.REJOICING IN OTHERS"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >REJOICING IN OTHERS" }]->(child);
```
