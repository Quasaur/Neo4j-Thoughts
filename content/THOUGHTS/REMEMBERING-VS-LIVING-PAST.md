---
name: "thought.REMEMBERING VS LIVING PAST"
alias: "Thought: Remembering Vs Living Past"
type: THOUGHT
en_content: There's no sin in remembering the past...only in trying to live in it.
parent: topic.WISDOM
tags:
  - past
  - memory
  - attitude
  - sin
  - character
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.REMEMBERING VS LIVING PAST",
    alias: "Thought: Remembering Vs Living Past",
    parent: "topic.ATTITUDE",
    tags: ['past', 'memory', 'attitude', 'sin', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.REMEMBERING VS LIVING PAST",
    en_title: "Remembering Vs Living Past",
    en_content: "There's no sin in remembering the past...only in trying to live in it.",
    es_title: "Recordar Vs Vivir en el Pasado",
    es_content: "No hay pecado en recordar el pasado...solo en tratar de vivir en él.",
    fr_title: "Se Souvenir Vs Vivre dans le Passé",
    fr_content: "Il n'y a pas de péché à se souvenir du passé...seulement à essayer d'y vivre.",
    hi_title: "स्मरण बनाम अतीत में जीना",
    hi_content: "अतीत को याद रखने में कोई पाप नहीं है...केवल उसमें जीने की कोशिश करने में है।",
    zh_title: "Jì Yì Yǔ Huó Zài Guò Qù",
    zh_content: "Jì zhù guò qù bìng bù shì zuì...zhǐ yǒu shì tú huó zài guò qù cái shì zuì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REMEMBERING VS LIVING PAST" AND c.name = "content.REMEMBERING VS LIVING PAST"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REMEMBERING VS LIVING PAST" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.REMEMBERING VS LIVING PAST"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->REMEMBERING VS LIVING PAST" }]->(child);
```
