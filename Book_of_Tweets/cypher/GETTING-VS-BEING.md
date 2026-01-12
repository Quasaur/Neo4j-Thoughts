---
name: "thought.GETTING VS BEING"
alias: "Thought: Getting Vs Being"
type: THOUGHT
en_content: We are more concerned with GETTING more than we are BEING more.
parent: topic.WISDOM
tags:
  - possession
  - character
  - getting
  - being
  - attitude
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Apr-2012a)
CREATE (t:THOUGHT {
    name: "thought.GETTING VS BEING",
    alias: "Thought: Getting Vs Being",
    parent: "topic.ATTITUDE",
    tags: ['possession', 'character', 'getting', 'being', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.GETTING VS BEING",
    en_title: "Getting Vs Being",
    en_content: "We are more concerned with GETTING more than we are BEING more.",
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
WHERE t.name = "thought.GETTING VS BEING" AND c.name = "content.GETTING VS BEING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GETTING VS BEING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.GETTING VS BEING"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >GETTING VS BEING" }]->(child);
```
