---
name: "thought.ESSENCE OF JOY"
alias: "Thought: Essence Of Joy"
type: THOUGHT
en_content: The essence of Joy is to discover that God is more wonderful, more great and more important than I.
parent: topic.ATTITUDE
tags:
  - joy
  - god
  - majesty
  - discovery
  - attitude
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.ESSENCE OF JOY",
    alias: "Thought: Essence Of Joy",
    parent: "topic.ATTITUDE",
    tags: ['joy', 'god', 'majesty', 'discovery', 'attitude'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ESSENCE OF JOY",
    en_title: "Essence Of Joy",
    en_content: "The essence of Joy is to discover that God is more wonderful, more great and more important than I.",
    es_title: "Esencia del Gozo",
    es_content: "La esencia del Gozo es descubrir que Dios es más maravilloso, más grande y más importante que yo.",
    fr_title: "Essence de la Joie",
    fr_content: "L'essence de la Joie est de découvrir que Dieu est plus merveilleux, plus grand et plus important que moi.",
    hi_title: "आनंद का सार",
    hi_content: "आनंद का सार यह खोजना है कि परमेश्वर मुझसे कहीं अधिक अद्भुत, महान और महत्वपूर्ण है।",
    zh_title: "Kuàilè de Běnzhì",
    zh_content: "Kuàilè de běnzhì jiùshì fāxiàn Shàngdì bǐ wǒ gèng qímiào, gèng wěidà, gèng zhòngyào."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ESSENCE OF JOY" AND c.name = "content.ESSENCE OF JOY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ESSENCE OF JOY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ESSENCE OF JOY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ESSENCE OF JOY" }]->(child);
```
