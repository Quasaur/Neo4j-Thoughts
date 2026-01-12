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
    es_title: "Obtener Vs Ser",
    es_content: "Estamos más preocupados por OBTENER más de lo que estamos por SER más.",
    fr_title: "Obtenir Vs Être",
    fr_content: "Nous sommes plus préoccupés par OBTENIR plus que nous le sommes par ÊTRE plus.",
    hi_title: "पाना बनाम होना",
    hi_content: "हम अधिक पाने की चिंता में अधिक होने की चिंता से ज्यादा व्यस्त हैं।",
    zh_title: "Dedao Yu Chenwei",
    zh_content: "Women geng guanxin DEDAO gengduo, er bu shi CHENWEI gengduo."
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
