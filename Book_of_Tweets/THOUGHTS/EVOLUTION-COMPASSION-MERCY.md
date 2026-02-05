---
name: "thought.EVOLUTION COMPASSION MERCY"
alias: "Thought: Evolution Compassion Mercy"
type: THOUGHT
en_content: "Can evolution explain Compassion? Mercy?"
parent: "topic.PHILOSOPHY"
tags:
- evolution
- compassion
- mercy
- philosophy
- science
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.EVOLUTION COMPASSION MERCY",
    alias: "Thought: Evolution Compassion Mercy",
    parent: "topic.PHILOSOPHY",
    tags: ['evolution', 'compassion', 'mercy', 'philosophy', 'science'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.EVOLUTION COMPASSION MERCY",
    en_title: "Evolution Compassion Mercy",
    en_content: "Can evolution explain Compassion? Mercy?",
    es_title: "Evolución, Compasión y Misericordia",
    es_content: "¿Puede la evolución explicar la Compasión? ¿La Misericordia?",
    fr_title: "Évolution, Compassion et Miséricorde",
    fr_content: "L'évolution peut-elle expliquer la Compassion ? La Miséricorde ?",
    hi_title: "विकास, करुणा और दया",
    hi_content: "क्या विकासवाद करुणा की व्याख्या कर सकता है? दया की?",
    zh_title: "Jìnhuà, bēimǐn, cíbēi  jìn huà ， bēi pī ， cí bēi",
    zh_content: "Jìnhuà lùn néng jiěshì bēimǐn ma? Cíbēi ne?  jìn huà lùn néng jiě shì bēi pī ma ？ cí bēi ne ？"
});

MATCH (t:THOUGHT {name: "thought.EVOLUTION COMPASSION MERCY"})
MATCH (c:CONTENT {name: "content.EVOLUTION COMPASSION MERCY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVOLUTION COMPASSION MERCY" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.EVOLUTION COMPASSION MERCY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->EVOLUTION COMPASSION MERCY" }]->(child);
```
