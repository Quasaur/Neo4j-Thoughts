---
name: "thought.DAMNING THE ARROGANT"
alias: "Thought: Damning The Arrogant"
type: THOUGHT
en_content: "How does God damn a sinner? By letting them prosper in their arrogance."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- judgment
- arrogance
- prosperity
- sovereignty
- god
level: 2
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-May-2012)
CREATE (t:THOUGHT {
    name: "thought.DAMNING THE ARROGANT",
    alias: "Thought: Damning The Arrogant",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'arrogance', 'prosperity', 'sovereignty', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DAMNING THE ARROGANT",
    en_title: "Damning The Arrogant",
    en_content: "How does God damn a sinner? By letting them prosper in their arrogance.",
    es_title: "Condenando al Arrogante",
    es_content: "¿Cómo condena Dios a un pecador? Dejándolos prosperar en su arrogancia.",
    fr_title: "Condamner l'Arrogant",
    fr_content: "Comment Dieu damne-t-Il un pécheur ? En le laissant prospérer dans son arrogance.",
    hi_title: "अहंकारी को दंडित करना",
    hi_content: "परमेश्वर एक पापी को कैसे दंडित करता है? उन्हें उनकी अहंकार में समृद्ध होने देता है।",
    zh_title: "Zhìzuì Jiāo'ào Zhě",
    zh_content: "Shàngdì zěnme zhìzuì yīgè zuìrén? Ràng tāmen zài tāmen de jiāo'ào zhōng fánróng."
});

MATCH (t:THOUGHT {name: "thought.DAMNING THE ARROGANT"})
MATCH (c:CONTENT {name: "content.DAMNING THE ARROGANT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DAMNING THE ARROGANT" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.DAMNING THE ARROGANT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY->DAMNING THE ARROGANT" }]->(child);
```
