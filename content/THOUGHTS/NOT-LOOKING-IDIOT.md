---
name: "thought.NOT LOOKING IDIOT"
alias: "Thought: Not Looking Idiot"
type: THOUGHT
en_content: I don't mind being an idiot, just looking like one.
parent: topic.WISDOM
tags:
  - idiot
  - appearance
  - attitude
  - character
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 04-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.NOT LOOKING IDIOT",
    alias: "Thought: Not Looking Idiot",
    parent: "topic.ATTITUDE",
    tags: ['idiot', 'appearance', 'attitude', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.NOT LOOKING IDIOT",
    en_title: "Not Looking Idiot",
    en_content: "I don't mind being an idiot, just looking like one.",
    es_title: "No Parecer Idiota",
    es_content: "No me importa ser un idiota, solo parecerlo.",
    fr_title: "Ne Pas Avoir l'Air Idiot",
    fr_content: "Cela ne me dérange pas d'être un idiot, juste d'en avoir l'air.",
    hi_title: "मूर्ख न दिखना",
    hi_content: "मुझे मूर्ख होने से कोई परेशानी नहीं है, बस मूर्ख दिखने से है।",
    zh_title: "Bu Xiang Kan Qi Lai Xiang Sha Gua",
    zh_content: "Wo Bu Jie Yi Dang Sha Gua, Zhi Shi Bu Xiang Kan Qi Lai Xiang Sha Gua."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NOT LOOKING IDIOT" AND c.name = "content.NOT LOOKING IDIOT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NOT LOOKING IDIOT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.NOT LOOKING IDIOT"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->NOT LOOKING IDIOT" }]->(child);
```
