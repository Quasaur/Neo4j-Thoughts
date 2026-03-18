---
type: THOUGHT
name: "thought.EVOLUTION COMPASSION MERCY"
alias: "Thought: Evolution Compassion Mercy"
parent: "topic.PHILOSOPHY"
en_content: "Can evolution explain Compassion? Mercy?"
tags: ["evolution", "compassion", "mercy", "philosophy", "science"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 31-Aug-2013)
CREATE (t:THOUGHT {    name: "thought.EVOLUTION COMPASSION MERCY",
    alias: "Thought: Evolution Compassion Mercy",
    parent: "topic.PHILOSOPHY",
    tags: ['evolution', 'compassion', 'mercy', 'philosophy', 'science'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.EVOLUTION COMPASSION MERCY",
    ctype: "THOUGHT",
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

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EVOLUTION COMPASSION MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->EVOLUTION COMPASSION MERCY"
RETURN t, parent;
```
